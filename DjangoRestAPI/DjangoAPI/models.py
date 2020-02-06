from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
# Create your models here.


STATUS_CHOICES = (
    ("Not Validated", "Not Validated"),
    ("Validated", "Validated"),
    ("Resolved", "Resolved")
)

EVENT_TYPE = (
    ('CONSTRUCTION', 'CONSTRUCTION'),
    ('SPECIAL_EVENT', 'SPECIAL_EVENT'),
    ('INCIDENT', 'INCIDENT'),
    ('WEATHER_CONDITION', 'WEATHER_CONDITION'),
    ('ROAD_CONDITION', 'ROAD_CONDITION')
)

User = get_user_model()


class Event(models.Model):
    Author = models.CharField(max_length=30)
    Location = models.PointField()
    CreationDate = models.DateField()
    ModDate = models.DateField()
    Description = models.CharField(max_length=100, default='Insert Description...')
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Validated')
    EventType = models.CharField(max_length=20, choices=EVENT_TYPE, verbose_name="EVENT_TYPE")

    def __str__(self):
        return self.Author

