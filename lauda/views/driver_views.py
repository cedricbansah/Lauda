from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from lauda.forms import driver_forms
from lauda.forms.driver_forms import DriverForm
from lauda.models import Driver


# @login_required(login_url='login')
def create_driver(request):
    if request.method == 'POST':

        form = DriverForm(request.POST)

        if form.is_valid():
            user = request.user
            driver = Driver.objects.create(user=user)
            # driver.license_number = form.cleaned_data['license_number']
            # driver.date_of_birth = form.cleaned_data['date_of_birth']
            # driver.address = form.cleaned_data['address']
            # driver.phone_number = form.cleaned_data['phone_number']

            driver.save()
            return redirect('index')

    else:
        user = request.user
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
        }
        form = DriverForm(initial=initial_data)

    return render(request, 'driver_profile.html', {"form": form})
