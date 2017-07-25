# -*- coding: utf-8 -*-
from datetime import datetime

from file_recording.user_registration.models import Session
from file_recording.user_registration.models import User


def user_login(user: User):
    user.is_login = True
    session = Session(user=user)
    session.save()
    user.save()
    return session


def user_logout(user: User, session: Session):
    user.is_login = False
    user.save()
    session.logout_at = datetime.now()
    session.auto_logout = False
    session.save()
