from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone


from .forms import PlaceForm
from .models import Place


def index(request):
    latest_place_list = Place.objects.order_by('-add_date')[:5]
    template = loader.get_template('religos/index.html')
    context = {
        'latest_place_list': latest_place_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'religos/detail.html', {'place': place})


def edit(request, place_id):
    return HttpResponse("You'er editing at place %s" % place_id)


def add(request):
    if request.method == 'POST':
        try:
            form = PlaceForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                phone_number = form.cleaned_data['phone_number']
                location = form.cleaned_data['location']
                place = Place()
                place.name = name
                place.phone_number = phone_number
                place.location = location
                place.add_date = timezone.now()
                place.save()
                reverser = reverse('religos:detail', args=(place.id,))
                return HttpResponseRedirect(reverser)
        except:
            raise
    else:
        form = PlaceForm()
        return render(request, 'religos/add.html', {'form': form})
