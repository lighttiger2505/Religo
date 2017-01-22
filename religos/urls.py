from django.conf.urls import url

from . import views

app_name = "religos"
urlpatterns = [
    # ex: /religos/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /religos/5/
    url(r'^(?P<place_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /religos/5/edit/
    url(r'^(?P<place_id>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /religos/add/
    url(r'^add/$', views.add, name='add'),
    # ex: /religos/upload_file/
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    # ex: /religos/5/upload_complate
    url(
        r'^(?P<photo_id>[0-9]+)/complete_upload/$',
        views.complete_upload,
        name='complete_upload'
    ),
]
