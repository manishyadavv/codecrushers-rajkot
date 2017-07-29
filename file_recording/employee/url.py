# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.employee.views import create_admin
from file_recording.employee.views import login_employee

urlpatterns = [
    url(r'create$', create_admin),
    url(r'login$', login_employee)
]
