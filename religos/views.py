from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Religo index.")

def detail(request, place_id):
    return HttpResponse("You'er looking at place %s" %place_id)

def edit(request, place_id):
    return HttpResponse("You'er editing at place %s" %place_id)

def add(request):
    return HttpResponse("You'er adding at place")
