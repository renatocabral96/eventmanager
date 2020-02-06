from rest_framework import serializers
from .models import Event

# Serializer class to allow models to be presented in JSON format
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
