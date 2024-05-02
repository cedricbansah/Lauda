from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from lauda.models import Driver
from lauda.utils.show_errors import show_error


# @login_required(login_url="login")
def vehicle_view(request):
    if "user_id" not in request.session:
        return redirect(reverse('login'))

    try:
        driver = Driver.objects.get(id=request.session['user_id'])
    except Driver.DoesNotExist:
        return show_error(request, 'Driver Does Not Exist')

    driver_vehicle = driver.vehicle_assigned

    return render(request, 'vehicle_info.html', {'driver_vehicle': driver_vehicle})