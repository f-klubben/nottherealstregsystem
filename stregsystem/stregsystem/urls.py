from django.conf.urls import include, url
from django.contrib import admin
from stregsystem.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quick/', quick)
]
