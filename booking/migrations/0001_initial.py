# Generated by Django 5.0.2 on 2024-08-27 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, validators=[django.core.validators.EmailValidator()])),
                ('phone', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('location', models.CharField(default='No location', max_length=255)),
                ('message', models.CharField(default='No message', max_length=255)),
                ('submitted_date', models.DateField(blank=True, null=True)),
                ('submitted_time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
