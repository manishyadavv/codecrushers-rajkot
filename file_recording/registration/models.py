import hashlib

from django.db import models

from file_recording.employee.models import Admin
from file_recording.schemes.models import Flat
from file_recording.user.models import User
# Create your models here.


class Registration(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=False, blank=False, related_name='applications')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE,
                             null=False, blank=False, related_name='registrations')
    registration_id = models.CharField(max_length=40)
    is_verified = models.BooleanField(default=False)
    bank_name = models.CharField(max_length=100)
    bank_branch_name = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=20)
    joint_application = models.BooleanField(default=False)
    bank_account_no = models.CharField(max_length=20)

    verified_by = models.ForeignKey(
        Admin, on_delete=models.CASCADE, null=True, blank=False)
    is_valid = models.NullBooleanField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.registration_id = hashlib.sha1(
            str(self.user.name + str(self.flat.id)).encode('utf-8')).hexdigest()
        super(Registration, self).save(*args, **kwargs)
