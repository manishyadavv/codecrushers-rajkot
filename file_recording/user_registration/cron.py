# -*- coding: utf-8 -*-
from datetime import datetime

import cronjobs

from file_recording.constants.constants import LOGOUT_TIMEOUT_SECONDS
from file_recording.user_registration.models import Session
from file_recording.user_registration.utils import user_logout


@cronjobs.register
def auto_logout():
    sessions = Session.objects.filter(logout_at=None)
    for session in sessions:
        if (datetime.now() - session.created_at).total_seconds() > LOGOUT_TIMEOUT_SECONDS:
            user_logout(session.user, session, True)
