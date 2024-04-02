from datetime import datetime, timedelta

def get_yesterday_datetime() -> str:
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime('%A, %d. %B, %Y. ')

def current_date_and_time():
    return datetime.now().strftime("%A, %d. %B, %Y. %H:%M")

