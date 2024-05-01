from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from lauda.models import Driver


# @login_required(login_url="login")
def vehicle_view(request):
    if "user_id" not in request.session:
        return redirect(reverse('login'))

    try:
        driver = Driver.objects.get(id=request.session['user_id'])
    except Driver.DoesNotExist:
        return redirect(reverse('404'))

    driver_vehicle = driver.vehicle_assigned

    return render(request, 'vehicle_info.html', {'driver_vehicle': driver_vehicle})