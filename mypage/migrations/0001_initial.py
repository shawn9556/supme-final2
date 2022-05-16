# Generated by Django 4.0.4 on 2022-05-12 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone_number', models.CharField(max_length=32)),
                ('gender', models.CharField(choices=[('M', '남성'), ('W', '여성')], max_length=4)),
                ('email', models.CharField(max_length=32)),
                ('age', models.CharField(max_length=4)),
                ('alien_type', models.CharField(max_length=32)),
                ('alien_content', models.TextField()),
                ('for_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('travel_purpose', models.CharField(choices=[('힐링', '힐링'), ('아웃도어', '아웃도어'), ('맛집투어', '맛집투어'), ('자연감상', '자연감상')], default='자연감상', max_length=30)),
                ('selection_state', models.CharField(choices=[('preparing', '여행 준비 중'), ('prepared', '여행 준비 끝'), ('on_travel', '여행 중'), ('finish', '여행 끝')], default='preparing', max_length=32)),
                ('place_start', models.CharField(choices=[('강동구', '강동구'), ('강남구', '강남구'), ('강북구', '강북구'), ('강서구', '강서구')], default='강동구', max_length=10)),
                ('create_date', models.DateTimeField()),
                ('selector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mypage.profile')),
            ],
        ),
    ]