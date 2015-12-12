from django.conf.urls import patterns, include, url

from django.contrib import admin
from api import views as api_view

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', api_view.Home.as_view()),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include("api.urls")),

)
