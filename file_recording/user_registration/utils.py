from datetime import datetime

from file_recording.user_registration.models import LoginLog
from file_recording.user_registration.models import User


def user_login(user: User):
    user.is_login = True
    LoginLog(user=user, login_time=datetime.now()).save()
    user.save()
