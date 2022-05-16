# Generated by Django 4.0.4 on 2022-05-13 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel_box',
            name='travel_box_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]