# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.document import views

urlpatterns = [
    url(r'doc_types', views.doc_types),
    url(r'upload', views.upload_file),
    url(r'get_doc', views.get_file)
]
