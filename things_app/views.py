from django.shortcuts import render
from rest_framework import generics, permissions
from .models import thing
from .serializers import thingSeralizer
# Create your views here.

class ThingsList(generics.ListCreateAPIView): 
  queryset = thing.objects.all() 
  seralizer_class = thingSeralizer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = thing.objects.all()
    serializer_class = thingSerializer