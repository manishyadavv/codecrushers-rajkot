# -*- coding: utf-8 -*-
"""file_recording URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

from file_recording.document.urls import urlpatterns as document_urls
from file_recording.employee.url import urlpatterns as employee_urls
from file_recording.registration.urls import urlpatterns as registeration_urls
from file_recording.result.urls import urlpatterns as result_urls
from file_recording.schemes.urls import urlpatterns as scheme_urls
from file_recording.updates.urls import urlpatterns as notification_urls
from file_recording.user.urls import urlpatterns as user_urls
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include(user_urls)),
    url(r'^notifications/', include(notification_urls)),
    url(r'^scheme/', include(scheme_urls)),
    url(r'^registeration/', include(registeration_urls)),
    url(r'^documents/', include(document_urls)),
    url(r'^employee/', include(employee_urls)),
    url(r'^result/', include(result_urls))
]  # +static()
