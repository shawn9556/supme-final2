# Generated by Django 4.0.4 on 2022-05-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbox', '0010_rename_accomdation_travel_box_accomdation_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel_box',
            name='traffic_road',
            field=models.ImageField(blank=True, null=True, upload_to='landing/images/%Y/%m/%d/%H/'),
        ),
    ]
