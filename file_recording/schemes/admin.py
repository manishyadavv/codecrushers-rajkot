from django.contrib import admin

from file_recording.schemes.models import Flat
from file_recording.schemes.models import FlatType
from file_recording.schemes.models import Scheme
# Register your models here.

admin.site.register(Scheme)
admin.site.register(Flat)
admin.site.register(FlatType)
