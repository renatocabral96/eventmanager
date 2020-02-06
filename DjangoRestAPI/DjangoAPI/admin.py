from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Event

# Register your models here.


@admin.register(Event)
class EventAdmin(OSMGeoAdmin):
    list_display = ("Author", "Location", "CreationDate", "ModDate", "Status", "EventType")
    list_filter = ("Author", "EventType", "Location")
