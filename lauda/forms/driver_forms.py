from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput, BooleanField, TextInput

from lauda.models import Driver


class DriverForm(ModelForm):
    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password confirmation', widget=PasswordInput)
    # is_active = BooleanField(label='Is active')

    class Meta:
        model = Driver
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'date_of_birth',
                  'license_number',
                  'address',
                  'password1',
                  'password2', ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        driver = super().save(commit=False)
        driver.set_password(self.cleaned_data["password1"])
        if commit:
            driver.save()
        return driver


class ResetPasswordForm(forms.Form):
    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password confirmation', widget=PasswordInput)
    # is_active = BooleanField(label='Is active')

    class Meta:
        model = Driver
        fields = ['password1',
                  'password2']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    # def save(self, commit=True):
    #     try:
    #         driver = Driver.objects.get(id=self.cleaned_data["driver_id"])
    #     except Driver.DoesNotExist:
    #         raise ValidationError("Driver does not exist")
    #     driver.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         driver.save()
    #     return driver


class ForgotPasswordForm(forms.Form):
    email = CharField(label='Email', widget=TextInput(attrs={'placeholder': 'Email'}))

