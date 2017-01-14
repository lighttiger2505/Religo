from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(label='名称', max_length=200)
    phone_number = forms.CharField(label='電話番号', max_length=100)
    location = forms.CharField(label='住所', max_length=200)
