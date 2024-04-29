from django import forms
from django.core.validators import RegexValidator

from lauda.models import Vehicle


class VehicleCreationForm(forms.ModelForm):
    class Meta:
        model = Vehicle

    # choices for vehicle type
    HATCHBACK = "Hatchback"
    SEDAN = "Sedan"
    SUV = "SUV"
    MINIVAN = "Minivan"
    PICK_UP = "Pick-Up Truck"

    VEHICLE_TYPES = (
        (HATCHBACK, "Hatchback"),
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (MINIVAN, "Minivan"),
        (PICK_UP, "Pick-Up Truck")
    )

    # options for vehicle status
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    STATUS_OPTIONS = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive")
    )

    license_plate_regex = r'^[A-Z]{2}-\d{1,4}-\b[A-Z|\d{2}]$'
    license_plate_validator = RegexValidator(
        regex=license_plate_regex,
        message='License plate must be either XY-0000-00 or AB-000-X',
        code='Invalid license plate number'
    )

    # fields = ['__all__']

    make = forms.CharField(required=True, max_length=50)
    model = forms.CharField(required=True, max_length=50)
    year = forms.IntegerField(required=True)
    license_plate = forms.CharField(required=True, max_length=50, validators=[license_plate_validator])
    color = forms.CharField(required=True, max_length=50)
    vehicle_type = forms.ChoiceField(required=True, choices=VEHICLE_TYPES)
    vehicle_status = forms.ChoiceField(default=ACTIVE, choices=STATUS_OPTIONS)

    def clean_year(self):
        year = self.cleaned_data['year']
        if year < 1900 or year > 2025:
            raise forms.ValidationError("Year must be between 1900 and 2025")
        return year
