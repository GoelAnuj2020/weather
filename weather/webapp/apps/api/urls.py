from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',

    url(r"^home/", views.Home.as_view(), name='test'),
    url(r"^weather/", views.Weather.as_view(), name='test'),
)