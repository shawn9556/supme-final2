# Generated by Django 4.0.4 on 2022-05-17 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelbox', '0008_getpic_getpic_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getpic',
            name='getpic_user',
        ),
    ]
