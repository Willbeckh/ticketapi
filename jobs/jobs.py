from django.conf import settings
from datetime import datetime as dt
from tickets import models
import logging
import pytz

TIME_ZONE = pytz.timezone('Africa/Nairobi')


def get_time_diff_hrs(start, stop):
    """this method gets the time difference in hours for two datetime objects."""
    time_diff = start - stop
    diff_in_hrs = time_diff.total_seconds() / 3600
    return int(diff_in_hrs)


def schedule_api():
    tickets = models.Ticket.objects.all()
    time_today = dt.now(TIME_ZONE)

    for ticket in tickets:
        date_created = ticket.created_at
        time_diff = get_time_diff_hrs(time_today, date_created)
        if time_diff > 3:
            return ticket.delete()
        return ticket
