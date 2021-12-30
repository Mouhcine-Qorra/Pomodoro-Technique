import time
import datetime
from plyer import notification

total = start = datetime.datetime.now()
end = start + datetime.timedelta(seconds=25)

while True:
    if datetime.datetime.now() > end:
        notification.notify(title="Please take a short Break",
                            message="You Have studied for 25 Minutes, Take 5min Breaks! (Pomodoro Technique)",
                            app_icon="pngme.ico",
                            timeout=10
                            )

        # sleep 5min (5x60=300)
        t_time = datetime.datetime.now()-total
        print(f"You have Studied for {str(t_time).split('.')[0]}")
        time.sleep(300)

        end = end + datetime.timedelta(minutes=25)
