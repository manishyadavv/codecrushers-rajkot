from django.conf.urls import url

from file_recording.user_registration import views

urlpatterns = [
    url(r'register$', views.register_user, name='user_registration'),
    url(r'login$', views.login_user, name='user_login')
]