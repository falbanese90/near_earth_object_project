import datetime


def cd_to_datetime(calendar_date):
    return datetime.datetime.strptime(calendar_date, "%Y-%b-%d %H:%M")


def datetime_to_str(dt):
    return datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M")
