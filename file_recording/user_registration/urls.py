# -*- coding: utf-8 -*-
from django.conf.urls import url

from file_recording.user_registration import views

urlpatterns = [
    url(r'register$', views.register_user, name='user_registration'),
    url(r'login$', views.login_user, name='user_login'),
    url(r'logout$', views.logout_user, name='user_logout'),
    url(r'info', views.user_details, name='user_info')
]
