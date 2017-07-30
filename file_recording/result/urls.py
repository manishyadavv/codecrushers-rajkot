# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.result.views import allocate_flat
from file_recording.result.views import get_result

urlpatterns = [
    url(r'$', get_result),
    url(r'validate$', allocate_flat)
]
