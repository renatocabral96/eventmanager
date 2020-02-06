from django.forms import ModelForm
from .models import Event


def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['EventType']
