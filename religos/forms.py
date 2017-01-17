from django.forms import ModelForm
from django import forms

from religos.models import Place
from religos.models import Photo


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'phone_number', 'location']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


# class PhotoForm(ModelForm):
#     class Meta:
#         model = Photo
#         fields = ['name', 'img']

class PhotoForm(forms.Form):
    file = forms.FileField(
        label='Select a file'
    )
