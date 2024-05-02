from urllib.parse import parse_qs

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from mailjet_rest import Client

from fleet_management_system import settings

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from lauda.forms.auth_forms import LoginForm

from lauda.forms.driver_forms import *
from lauda.models import Driver


# Register a new user
def register_user(request):
    # Logic for when the form has been submitted
    if request.method == "POST":
        # form = UserRegistrationForm(data=request.POST)
        form = DriverForm(data=request.POST)

        # validate form before saving user
        if form.is_valid():
            driver = form.save()
            driver.is_active = False
            driver.save()
            mailjet = Client(auth=(settings.MAILJET_API_KEY,
                                   settings.MAILJET_API_SECRET), version='v3.1')

            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": 'cedibans@gmail.com',
                            "Name": "Cedric Bansah"
                        },
                        "To": [
                            {
                                "Email": request.POST['email'],
                                "Name": f"{request.POST['first_name']} {request.POST['last_name']}"
                            }
                        ],
                        "Subject": "Lauda Email Verification",
                        "HTMLPart": f"Please click here to verify your email: http://localhost:8000/email_verification?id={driver.id}",

                    }
                ]
            }

            mailjet.send.create(data=data)

            return redirect(reverse("email_confirmation"))
        print(form.errors)
        return redirect(reverse("404"))
    else:
        form = DriverForm()

    return render(request, "django_registration/registration_form.html", {'form': form})


def login(request):
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            login_form.clean()
            user = login_form.get_user()
            request.session['user_id'] = user.id
            login_form.confirm_login_allowed(user)

            if user.is_staff:
                return redirect(reverse("manager_dashboard"))

            return redirect(reverse("vehicle_info"))
            # username = request.POST['username']
            # password = request.POST['password']
        else:
            login_form.get_invalid_login_error()

    else:
        login_form = LoginForm()

    return render(request, "django_registration/login_form.html", {'form': login_form})


def verify_email(request):
    driver_id = request.GET.get('id')

    if driver_id:
        try:
            driver = Driver.objects.get(id=driver_id)

        except Driver.DoesNotExist:
            return redirect(reverse("404"))

        driver.is_active = True
        driver.save()
        return redirect(reverse("login"))

    return redirect(reverse("404"))


def confirm_email(request):
    return render(request, 'django_registration/email_confirmation.html')


def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                driver = Driver.objects.get(email=email)
            except Driver.DoesNotExist:
                return redirect(reverse("404"))

            mailjet = Client(auth=(settings.MAILJET_API_KEY,
                                   settings.MAILJET_API_SECRET), version='v3.1')

            token_generator = PasswordResetTokenGenerator()
            password_token = token_generator.make_token(driver)

            params = f'driver_id={driver.id}&token={password_token}'
            encrypted_params = urlsafe_base64_encode(force_bytes(params))
            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": 'cedibans@gmail.com',
                            "Name": "LAUDA"
                        },
                        "To": [
                            {
                                "Email": request.POST['email'],
                                "Name": driver.get_full_name()
                            }
                        ],
                        "Subject": "Lauda Email Verification",
                        "HTMLPart": f"Please click here to reset your password: http://localhost:8000/reset_password?data={encrypted_params}",

                    }
                ]
            }

            mailjet.send.create(data=data)
            print(form.errors)
            return redirect(reverse("forgot_password_confirmation"))

    form = ForgotPasswordForm()

    return render(request, 'django_registration/forgot_password.html', {"form": form})


def reset_password(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            try:
                driver = Driver.objects.get(pk=request.POST['driver_id'])
            except Driver.DoesNotExist:
                return redirect(reverse('404'))
            driver.set_password(request.POST['password1'])
            driver.save()
            # print(form.errors)
            return redirect(reverse("login"))

    data = request.GET.get('data')

    # print("hello cnana")
    if not data:
        return redirect(reverse('404'))

    # Decode the URL-safe base64 encoded string
    decoded_bytes = urlsafe_base64_decode(data)
    decoded_str = decoded_bytes.decode('utf-8')

    # Parse the decoded string into key-value pairs
    parsed_params = parse_qs(decoded_str)

    # Convert the parsed parameters to a dictionary
    params_dict = {key: value[0] for key, value in parsed_params.items()}
    print(params_dict)

    password_token = params_dict['token']
    driver_id = params_dict['driver_id']

    form = ResetPasswordForm()

    return render(request, 'django_registration/reset_password.html',
                  {"form": form, "token": password_token, "driver_id": driver_id})


def forgot_password_confirmation(request):
    return render(request, 'django_registration/forgot_password_confirmation.html')
