from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from lauda.forms import driver_forms
from lauda.forms.driver_forms import DriverForm
from lauda.models import Driver, Vehicle
from lauda.utils.show_errors import show_error


def driver_dashboard(request):

    if 'user_id' not in request.session:
        return redirect('login')
    print(request.session['user_id'])
    try:
        driver = Driver.objects.get(id=request.session['user_id'])  # Assuming authenticated user is a Driver instance
    except Driver.DoesNotExist:
        return show_error(request, 'Driver Does Not Exist')

    vehicles_assigned = driver.vehicles.all()  # Efficiently retrieve all assigned vehicles
    context = {
        'assigned_vehicles': vehicles_assigned,
        'user': driver
    }
    return render(request, 'driver_dashboard.html', context)


    # driver = Driver.objects.get(pk=request.session['user_id'])
    # print(driver)
    # vehicles_assigned = [Vehicle.objects.get(driver_assigned=driver.license_number)]
    #
    # context = {
    #     'vehicles_assigned': vehicles_assigned,
    # }
    #
    #
    # return render(request, 'driver_dashboard.html', context)

    # if request.method == 'POST':
    #
    #     form = DriverForm(request.POST)
    #
    #     if form.is_valid():
    #         user = request.user
    #         driver = Driver.objects.create(user=user)
    #         driver.save()
    #         return redirect('index')
    #
    # else:
    #     user = request.user
    #     initial_data = {
    #         'first_name': user.first_name,
    #         'last_name': user.last_name,
    #         'username': user.username,
    #         'email': user.email,
    #     }
    #     form = DriverForm(initial=initial_data)
    #     # return redirect()
    #
    # return render(request, 'driver_dashboard.html', {"form": form})
