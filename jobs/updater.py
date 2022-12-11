from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api


def start():
    """This method, creates a background schedule instance and uses it to schedule tasks within intervals"""

    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_api, 'interval', minutes=15)
    scheduler.start()
