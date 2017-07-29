# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.employee.views import create_admin

urlpatterns = [
    url(r'create', create_admin),
]
