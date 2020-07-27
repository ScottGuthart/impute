from flask import current_app
import os
from datetime import datetime
from pytz import timezone
from time import strftime, localtime


def save_user_file(user, data, name, ext, save=True):
    if not os.path.exists(current_app.instance_path):
        os.mkdir(current_app.instance_path)
    if not os.path.exists(os.path.join(current_app.instance_path, "files")):
        os.mkdir(os.path.join(current_app.instance_path, "files"))
    if not os.path.exists(
        os.path.join(current_app.instance_path, "files", user.username)
    ):
        os.mkdir(os.path.join(current_app.instance_path, "files", user.username))
    filename = os.path.join(
        current_app.instance_path, "files", user.username, f"{name}.{ext}"
    )
    if data and save:
        data.save(filename)
    return filename


def utc_to_human_readable(utc, query_string=False):
    if query_string:  # expected to come as a float
        utc_float_as_time = localtime(utc)
        return strftime("%Y%m%d,%H%M%S", utc_float_as_time)
    return utc.strftime("%Y-%m-%d %I%M%S%p")  # comes as a datetime


def get_time_string(for_autoversioning=False):
    localized_time = (
        timezone("utc")
        .localize(datetime.utcnow())
        .astimezone(timezone("US/Eastern"))
        .replace(tzinfo=None)
    )
    return utc_to_human_readable(localized_time, for_autoversioning)
