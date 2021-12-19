from time import sleep
from datetime import datetime, timedelta

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

def stop(minute : int):
    sleep((minute * 60))

def now() -> datetime:
    return datetime.now()

def minutes_before_now(minute : int):
    return now() - timedelta(minutes = minute)

def time_format(time : datetime, format = DEFAULT_DATE_FORMAT) -> str:
    return time.strftime(format)

def between_time(time : datetime, start_time : datetime, end_time : datetime) -> bool:
    return start_time < time and time < end_time

def create_time_from_today(hour : int, minute : int) -> datetime:
    return now().replace(hour = hour, minute = minute, second = 0)
