from django.forms import ModelForm
from django import forms

from religos.models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'phone_number', 'location']
        labels = {
            'name': '店名',
            'phone_number': '電話番号',
            'location': '住所',
        }
        help_texts = {
            'name': '店名を入力してください。',
            'phone_number': '電話番号を入力してください。例：xxxx-xx-xxxx',
            'location': '住所を入力してください。例：◯◯県◯◯市◯◯町x-x-x',
        }
        error_messages = {
            'name': {
                'max_length': "This writer's name is too long.",
                'required': "必須入力項目です。",
            }
        }


class PhotoForm(forms.Form):
    file = forms.FileField(
        label='Select a file'
    )


class LoginForm(forms.Form):
    username = forms.fields.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
