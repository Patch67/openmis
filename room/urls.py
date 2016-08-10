from django.conf.urls import url
from . import views

app_name = 'room'

urlpatterns = [
    url(r'^(?P<room_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
