# Generated by Django 4.2.11 on 2024-04-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10)),
                ('license_number', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=255, unique=True)),
                ('color', models.CharField(max_length=255)),
                ('vehicle_type', models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Minivan', 'Minivan'), ('Pick-Up Truck', 'Pick-Up Truck')], max_length=255)),
                ('vehicle_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
            ],
        ),
    ]
