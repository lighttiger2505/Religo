from django.forms import ModelForm


from religos.models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['id', 'name', 'phone_number', 'location']
