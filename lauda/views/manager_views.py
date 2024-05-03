from django.core.serializers import serialize
from django.db import IntegrityError
from django.db.models import Count, When, Case, IntegerField, Q
from django.shortcuts import render, redirect
from django.urls import reverse
import pandas as pd

from lauda.models import Driver, User, Vehicle
from lauda.utils.show_errors import show_error


def manager_view(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_vehicles = request.FILES['file']
        is_cancelled = request.POST.get('is_cancelled') == '1'
        if is_cancelled:
            return redirect('manager_dashboard')
        else:
            data = pd.read_excel(uploaded_vehicles)
            vehicle_list = []
            for index, row in data.iterrows():
                make = row['Make']
                model = row['Model']
                year = row['Year']
                license_plate = row['License Plate']
                color = row['Color']
                vehicle_type = row['Vehicle Type']

                vehicle_list.append(Vehicle(
                    make=make,
                    model=model,
                    year=year,
                    license_plate=license_plate,
                    color=color,
                    vehicle_type=vehicle_type
                ))
        Vehicle.objects.bulk_create(vehicle_list, ignore_conflicts=True)

    if "user_id" not in request.session:
        return redirect(reverse('login'))

    try:
        manager = User.objects.get(id=request.session['user_id'])
    except User.DoesNotExist:
        return show_error(request, 'Driver Does Not Exist')

    if not manager.is_staff:
        return show_error(request, 'You do not have permission to view this page')

    all_vehicles = Vehicle.objects.all()
    all_drivers = Driver.objects.all()

    all_vehicles_json = serialize('json', all_vehicles)
    all_drivers_json = serialize('json', all_drivers)


    vehicles = all_vehicles.aggregate(
        total_vehicles=Count('id'),
        active_vehicles=Count(Case(When(vehicle_status='Active', then=1), output_field=IntegerField())),
        inactive_vehicles=Count(Case(When(vehicle_status='Inactive', then=1), output_field=IntegerField()))
    )
    # print(vehicles)

    vehicle_types = list(Vehicle.objects.values_list('vehicle_type', flat=True).distinct())

    vehicle_types_count = Vehicle.objects.aggregate(
        total_vehicles=Count('id'),
        **{''.join(char for char in vehicle_type if char.isalnum()) + '_count': Count('id', filter=Q(vehicle_type=vehicle_type)) for vehicle_type in vehicle_types}
    )
    # print(vehicle_types_count)
    # drivers = all_drivers.aggregate(
    #     total_drivers=Count('id'),
    #     assigned_drivers=Count(Case(When(vehicle_assigned__isnull=False, then=1), output_field=IntegerField())),
    #     unassigned_drivers=Count(Case(When(vehicle_assigned__isnull=True, then=1), output_field=IntegerField())),
    #
    # )

    active_vehicles = vehicles['active_vehicles']
    inactive_vehicles = vehicles['inactive_vehicles']
    total_vehicles = active_vehicles + inactive_vehicles
    # assigned_drivers = drivers['assigned_drivers']
    # unassigned_drivers = drivers['unassigned_drivers']
    # total_drivers = assigned_drivers + assigned_drivers

    context = {
        'all_drivers': all_drivers,
        'all_vehicles': all_vehicles,
        'vehicle_types': vehicle_types,
        'manager': manager,
        'total_vehicles': total_vehicles,
        'active_vehicles': active_vehicles,
        'inactive_vehicles': inactive_vehicles,
        'all_drivers_json': all_drivers_json,
        'all_vehicles_json': all_vehicles_json,
        # 'total_drivers': total_drivers,
        # 'assigned_drivers': assigned_drivers,
        # 'unassigned_drivers': unassigned_drivers,
        **vehicle_types_count

    }
    # print(all_drivers_json)

    return render(request, 'manager_view.html', context)


def update_assigned_driver(request, vehicle_id):
    if request.method == "POST":
        selected_driver = request.POST.get(f'assigned_driver-{vehicle_id}')

        vehicle = Vehicle.objects.get(pk=vehicle_id)

        vehicle.assigned_driver = selected_driver
        vehicle.save()

        return redirect(reverse('manager_dashboard'))

    return redirect(reverse('manager_view'))