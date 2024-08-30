import datetime
import time
from plyer import notification

while True:
    notification.notify(
        title=f"To-Do List - {datetime.date.today().strftime('%Y-%m-%d')}",
        message="1. Learn Python \n2. Projects \n3. Read Book \n4. Cyber Security",
        app_icon="F:/VS_CODING/Advance_PYTHON/Python Project/Images/notify.ico",
        timeout=5
    )
    time.sleep(30)
