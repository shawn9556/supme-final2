# Generated by Django 4.0.4 on 2022-05-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbox', '0005_remove_travel_box_travel_box_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel_box',
            name='create_date',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
