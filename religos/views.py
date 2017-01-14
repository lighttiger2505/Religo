from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render

from .models import Place


def index(request):
    latest_place_list = Place.objects.order_by('-add_date')[:5]
    template = loader.get_template('religos/index.html')
    context = {
        'latest_place_list': latest_place_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, place_id):
    try:
        place = Place.objects.get(pk=place_id)
    except:
        raise Http404("Place dose not exist")
    return render(request, 'religos/detail.html', {'place': place})


def edit(request, place_id):
    return HttpResponse("You'er editing at place %s" % place_id)


def add(request):
    return HttpResponse("You'er adding at place")
