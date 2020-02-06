# Generated by Django 3.0.2 on 2020-02-01 13:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loc', models.CharField(max_length=30)),
                ('Coord', django.contrib.gis.db.models.fields.PointField(help_text='Longitude, Latitude', srid=4326)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EVENT_TYPE',
            new_name='EventType',
        ),
        migrations.RemoveField(
            model_name='event',
            name='GeoLocation',
        ),
        migrations.AddField(
            model_name='event',
            name='GeoLocation',
            field=models.ManyToManyField(to='DjangoAPI.Location'),
        ),
    ]