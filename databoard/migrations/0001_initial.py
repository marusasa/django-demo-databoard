# Generated by Django 5.1.6 on 2025-02-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarometricPressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(help_text='Timestamp of the pressure reading.', unique=True)),
                ('pressure', models.FloatField(help_text='Barometric pressure in hectopascals (hPa).')),
            ],
            options={
                'verbose_name': 'Barometric Pressure',
                'verbose_name_plural': 'Barometric Pressures',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(help_text='Timestamp of the humidity reading.', unique=True)),
                ('humidity', models.IntegerField(help_text='Relative humidity as a percentage (0-100).')),
            ],
            options={
                'verbose_name': 'Humidity',
                'verbose_name_plural': 'Humidities',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('temperature', models.FloatField()),
            ],
        ),
    ]
