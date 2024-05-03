from io import BytesIO

from django.http import HttpResponse

from reportlab.lib.styles import ParagraphStyle

from lauda.models import Vehicle

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors


def export_to_pdf(request):
    # Retrieve all vehicles from the database
    vehicles = Vehicle.objects.all()

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="vehicle_report.pdf"'

    # Create a PDF Document
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer)
    elements = []

    data = [["Make", "Model", "Year", "License Plate", "Color", "Vehicle Type", "Vehicle Status", "Driver Assigned"]]

    for vehicle in vehicles:
        driver_name = vehicle.driver_assigned.name() if vehicle.driver_assigned else 'None'
        data.append([
            vehicle.make,
            vehicle.model,
            str(vehicle.year),
            vehicle.license_plate,
            vehicle.color,
            vehicle.get_vehicle_type_display(),
            vehicle.get_vehicle_status_display(),
            driver_name
        ])

    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    elements.append(table)

    doc.build(elements)

    pdf_data = pdf_buffer.getvalue()

    response.write(pdf_data)

    return response
