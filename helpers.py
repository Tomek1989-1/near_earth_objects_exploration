"""Convert datetimes to and from strings."""
import datetime


def cd_to_datetime(calendar_date):
    """Convert a NASA-formatted calendar date/time description into a datetime.

    :param calendar_date: A calendar date in YYYY-bb-DD hh:mm format,
    e.g. '2020-Dec-31 12:00'
    :return: A naive `datetime` corresponding to the given calendar
    date and time.,
    e.g. 'datetime.datetime(2020, 12, 31, 12, 0)'
    """
    return datetime.datetime.strptime(calendar_date, "%Y-%b-%d %H:%M")


def datetime_to_str(dt):
    """Convert a naive Python datetime into a human-readable string.

    :param dt: A naive Python datetime,
    e.g. 'datetime.datetime(2020, 12, 31, 12, 0)'
    :return: That datetime, as a human-readable string without seconds,
    e.g. ''2020-12-31 12:00''
    """
    return datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M")
