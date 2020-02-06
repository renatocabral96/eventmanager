from django.forms import ModelForm
from .models import Event


def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)

# Form class for event type choice rendering in HTML
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['EventType']
