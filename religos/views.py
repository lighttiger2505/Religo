from django.http import HttpResponse

def index(request):
    latest_place_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, place_id):
    return HttpResponse("You'er looking at place %s" %place_id)

def edit(request, place_id):
    return HttpResponse("You'er editing at place %s" %place_id)

def add(request):
    return HttpResponse("You'er adding at place")
