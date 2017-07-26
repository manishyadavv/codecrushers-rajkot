# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.schemes import views

urlpatterns = [
    url(r'scheme_get$', views.get_schemes),
    # url(r'create$', views.create_scheme)
]
