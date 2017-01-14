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
    edit_place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        try:
            form = PlaceForm(request.POST)
            if form.is_valid():
                edit_place = form.save(commit=False)
                edit_place.add_date = timezone.now()
                edit_place.save()
                reverser = reverse('religos:detail', args=(edit_place.id,))
                return HttpResponseRedirect(reverser)
        except:
            raise
    else:
        init_dict = dict(
            name=edit_place.name,
            phone_number=edit_place.phone_number,
            location=edit_place.location
        )
        form = PlaceForm(initial=init_dict)
        return render(
            request,
            'religos/edit.html',
            {'place_id': place_id, 'form': form}
        )


def add(request):
    if request.method == 'POST':
        try:
            form = PlaceForm(request.POST)
            if form.is_valid():
                new_place = form.save(commit=False)
                new_place.add_date = timezone.now()
                new_place.save()
                reverser = reverse('religos:detail', args=(new_place.id,))
                return HttpResponseRedirect(reverser)
        except:
            raise
    else:
        form = PlaceForm()
        return render(request, 'religos/add.html', {'form': form})
