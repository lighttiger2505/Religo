from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<place_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<place_id>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /polls/5/vote/
    url(r'^add/$', views.add, name='add'),
]
