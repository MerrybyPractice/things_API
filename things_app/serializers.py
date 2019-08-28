from .models import thing
from rest_framework import serializers

class thingSeralizer(serializers.ModelSerializer): 
  class Meta: 
    model = thing
    fields = ['title', 'belongs_to']