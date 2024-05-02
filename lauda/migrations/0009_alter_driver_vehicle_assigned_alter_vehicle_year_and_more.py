# Generated by Django 4.2.11 on 2024-05-02 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lauda', '0008_vehicle_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='vehicle_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver', to='lauda.vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='VerificationToken',
        ),
    ]