# Generated by Django 4.2.11 on 2024-05-02 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lauda', '0009_alter_driver_vehicle_assigned_alter_vehicle_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='vehicle_assigned',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='driver_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lauda.driver'),
        ),
    ]
