import pytz
from datetime import datetime as dt
from tickets import models

# Set the time zone to Africa/Nairobi
TIME_ZONE = pytz.timezone("Africa/Nairobi")


def get_time_diff_hrs(start: dt, stop: dt) -> int:
    """
    This method gets the time difference in hours for two datetime objects.

    Args:
        start: The starting datetime object.
        stop: The ending datetime object.

    Returns:
        An integer representing the number of hours between the two datetime objects.
    """
    time_diff = start - stop
    diff_in_hrs = time_diff.total_seconds() / 3600
    return int(diff_in_hrs)


def schedule_api():
    tickets = models.Ticket.objects.all()

    # Get the current time in the Africa/Nairobi time zone
    time_today = dt.now(TIME_ZONE)

    # Loop through all tickets
    for ticket in tickets:
        # Get the date and time when the ticket was created
        date_created = ticket.created_at

        # Calculate the number of hours between the current time and the time when the ticket was created
        time_diff = get_time_diff_hrs(time_today, date_created)

        # If the ticket is more than 3 hours old, delete it
        if time_diff > 3:
            ticket.delete()

    # Return the last ticket that was processed
    return ticket
