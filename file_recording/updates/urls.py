# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.updates import views

urlpatterns = [
    url(r'notifications$', views.notification, name='add_or_get_notifications'),
]
