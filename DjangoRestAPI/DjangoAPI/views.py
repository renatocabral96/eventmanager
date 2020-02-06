from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Event
from .serializer import EventSerializer
from django.shortcuts import render
from .forms import EventForm
from . import forms
# Create your views here.


# View that allows events to be filtered by author, location and type of event

def bootstrapFilterView(request):
    queryset = Event.objects.all()
    authorq = request.GET.get('author')
    locationq = request.GET.get('location')
    categoryq = request.GET.get('category')

    preset_form = forms.EventForm()

    if authorq != '' and authorq is not None:
        queryset = queryset.filter(Author__icontains=authorq)

    if locationq != '' and locationq is not None:
        queryset = queryset.filter(Location=locationq)

    if valid_param(categoryq) and categoryq != 'Choose...':
        queryset = queryset.filter(EventType__icontains=categoryq)

    context = {
        'queryset': queryset,
        'preset_form': preset_form
    }
    return render(request, "BootstrapFilter.html", context)


# Checks if an input parameter is valid

def valid_param(param):
    return param != '' and param is not None


# Allows viewing all the events that have been posted or create new ones

class AllEventView(ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Allows editing an event based on its id


class EventDetailsView(APIView):

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)