from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from mailjet_rest import Client

from fleet_management_system import settings
from lauda.forms import UserForm
from lauda.forms.auth_forms import UserRegistrationForm
from verify_email.email_handler import send_verification_email
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from lauda.forms.auth_forms import LoginForm
from django.contrib.auth.models import User

from lauda.forms.driver_forms import DriverForm
from lauda.models import VerificationToken, Driver
from lauda.serializers.auth_serializers.login_serializer import LoginSerializer
from lauda.serializers.auth_serializers.register_serializer import RegisterSerializer


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
            login_form.confirm_login_allowed(user)
            return redirect("driver_profile")
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