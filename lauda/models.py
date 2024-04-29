from datetime import datetime

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from lauda.managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def username(self):
        return None


class Vehicle(models.Model):
    # Model to represent a vehicle
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

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    STATUS_OPTIONS = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive")
    )

    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField
    license_plate = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=255)

    vehicle_type = models.CharField(
        max_length=255,
        choices=VEHICLE_TYPES
    )

    vehicle_status = models.CharField(
        max_length=10,
        choices=STATUS_OPTIONS,
        default=ACTIVE
    )

    #    driver_assigned = models.ForeignKey(Driver, to_field=registration_number, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.license_plate}"


class Driver(User):
    # Model to represent a driver
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=10)
    license_number = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    vehicle_assigned = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.license_number}"


# class User(AbstractUser):
#     class Meta(AbstractUser.Meta):
#         swappable = 'AUTH_USER_MODEL'
#
#     def __str__(self):
#         return f"{self.username} {self.email}"


class VerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
