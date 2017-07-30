# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.registration import views

urlpatterns = [
    url(r'register$', views.user_application),
]
