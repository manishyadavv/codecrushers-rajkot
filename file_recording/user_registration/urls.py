from django.conf.urls import url

from file_recording.user_registration import views

urlpatterns = [
    url(r'^register', views.register_user, name='user registration')
]
