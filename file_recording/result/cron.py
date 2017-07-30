# -*- coding: utf-8 -*-
import random
from datetime import datetime

from django_cron import CronJobBase

from file_recording.registration.models import Registration
from file_recording.result.models import DrawResult
from file_recording.result.utils import email
from file_recording.schemes.models import Scheme


class ResultDraw(CronJobBase):
    code = 'file_recording.result.ResultDraw'

    def allot_flats(self, flat):
        registrations = Registration.objects.filter(flat=flat)
        users = [
            registration.user for registration in registrations if registration.is_valid]
        random.shuffle(users)
        i = 1
        for user in users[:max([int(1.1 * flat.no_of_flats), flat.no_of_flats + 10])]:
            DrawResult(user=user, flat=flat, waiting_number=i,
                       scheme=flat.scheme).save()
            message = email.create_message(None, user, flat)
            email.send_message(None, message)
            i += 1

    def do(self):
        schemes = Scheme.objects.filter(draw_date=datetime.today())
        for scheme in schemes:
            for flat in scheme.flats:
                self.allot_flats(flat)
