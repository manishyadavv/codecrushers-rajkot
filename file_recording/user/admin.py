# -*- coding: utf-8 -*-
from django.contrib import admin

from file_recording.user.models import Session
from file_recording.user.models import User

# Register your models here.

admin.site.register(User)
admin.site.register(Session)
