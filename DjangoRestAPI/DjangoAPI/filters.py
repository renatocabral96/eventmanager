import django_filters
from DjangoAPI.models import Event

# Class selecting the fields to be used during the filtering process
class EventFilters(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ('Author', 'Location', 'Status')
