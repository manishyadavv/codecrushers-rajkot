# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.schemes import views

urlpatterns = [
    url(r'scheme_get$', views.get_schemes),
    url(r'create_scheme$', views.create_scheme),
    url(r'add_flat$', views.add_flats),
]
