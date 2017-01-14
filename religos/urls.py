from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /religos/
    url(r'^$', views.index, name='index'),
    # ex: /religos/5/
    url(r'^(?P<place_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /religos/5/edit/
    url(r'^(?P<place_id>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /religos/add/
    url(r'^add/$', views.add, name='add'),
]
