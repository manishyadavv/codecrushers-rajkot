# -*- coding: utf-8 -*-
from datetime import datetime

from django_cron import CronJobBase

from file_recording.constants.constants import LOGOUT_TIMEOUT_SECONDS
from file_recording.user.models import Session
from file_recording.user.utils import user_logout


class AutoLogout(CronJobBase):
    code = 'user.auto_logout'

    def do(self):
        sessions = Session.objects.filter(logout_at=None)
        for session in sessions:
            if (datetime.now() - session.created_at).total_seconds() > LOGOUT_TIMEOUT_SECONDS:
                user_logout(session.user, session, True)
