from django.http import HttpResponse
from openpyxl import Workbook

from lauda.models import Vehicle


def export_to_excel(request):
    # Create a new workbook
    wb = Workbook()
    ws = wb.active

    # Write data to the worksheet
    ws.append(["Make", "Model", "Year", "License Plate", "Color", "Vehicle Type", "Vehicle Status"])
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        ws.append([vehicle.make,
                   vehicle.model,
                   vehicle.year,
                   vehicle.license_plate,
                   vehicle.color,
                   vehicle.vehicle_type,
                   vehicle.vehicle_status])

    # Save the workbook to a BytesIO buffer
    from io import BytesIO
    buffer = BytesIO()
    wb.save(buffer)

    # Set response headers for Excel file download
    response = HttpResponse(buffer.getvalue(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Vehicle Data.xlsx"'

    return response