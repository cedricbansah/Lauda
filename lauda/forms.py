from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Vehicle, User
from django_registration.forms import RegistrationForm


# class CreateVehicleForm(forms.ModelForm):
#     # Form for creating a new vehicle
#
#     class Meta:
#         model = Vehicle
#         fields = ['year',
#                   'make',
#                   'model',
#                   'color',
#                   'license_plate',
#                   'vehicle_type',
#                   ]
#

# class UserForm(UserCreationForm):
#     # email = forms.EmailField()
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
#
#     class Meta(RegistrationForm.Meta):
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'username', '<PASSWORD>', '<PASSWORD>')
