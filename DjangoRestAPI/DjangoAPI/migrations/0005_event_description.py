# Generated by Django 3.0.2 on 2020-02-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAPI', '0004_auto_20200201_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Description',
            field=models.CharField(default='Insert Description...', max_length=100),
        ),
    ]
