# Generated by Django 4.0.4 on 2022-05-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_alter_select_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='select',
            name='people',
            field=models.IntegerField(),
        ),
    ]