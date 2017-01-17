from django.forms import ModelForm
from django import forms

from religos.models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'phone_number', 'location']


class PhotoForm(forms.Form):
    file = forms.FileField(
        label='Select a file'
    )
