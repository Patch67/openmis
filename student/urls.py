from django.conf.urls import url
from . import views

app_name = "student"

urlpatterns = [
    # /student/
    url(r'^$', views.index, name='index'),
    # /student/232/
    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    # /student/123/update/
    url(r'^(?P<student_id>[0-9]+)/update/$', views.detail, name='update'),
]
