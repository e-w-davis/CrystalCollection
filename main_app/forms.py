from ast import Mod
from dataclasses import field
from django.forms import ModelForm
from .models import Cleansing, Location

class CleansingForm(ModelForm):
    class Meta:
        model = Cleansing
        fields = ['date', 'method']

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'