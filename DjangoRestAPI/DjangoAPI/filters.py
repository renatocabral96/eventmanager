import django_filters
from DjangoAPI.models import Event


class EventFilters(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ('Author', 'Location', 'Status')
