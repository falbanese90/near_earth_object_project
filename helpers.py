"""Datetime formatter."""
import datetime


def cd_to_datetime(calendar_date):
    """Date to Datetime."""
    return datetime.datetime.strptime(calendar_date, "%Y-%b-%d %H:%M")


def datetime_to_str(dt):
    """Datetime to string."""
    return datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M")
