# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.employee.views import create_admin
from file_recording.employee.views import login_employee
from file_recording.user.views import validate_user

urlpatterns = [
    url(r'create$', create_admin),
    url(r'login$', login_employee),
    url(r'validate_user$', validate_user)
]
