# Generated by Django 3.0.2 on 2020-01-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GeoLocation', models.CharField(max_length=30)),
                ('Author', models.CharField(max_length=30)),
                ('CreationDate', models.DateField()),
                ('ModDate', models.DateField()),
                ('Status', models.CharField(choices=[('Not Validated', 'Not Validated'), ('Validated', 'Validated'), ('Resolved', 'Resolved')], default='Not Validated', max_length=20)),
                ('EVENT_TYPE', models.CharField(choices=[('CONSTRUCTION', 'CONSTRUCTION'), ('SPECIAL_EVENT', 'SPECIAL_EVENT'), ('INCIDENT', 'INCIDENT'), ('WEATHER_CONDITION', 'WEATHER_CONDITION'), ('ROAD_CONDITION', 'ROAD_CONDITION')], max_length=20)),
            ],
        ),
    ]
