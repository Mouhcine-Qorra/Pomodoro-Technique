import time
import datetime
from plyer import notification


total = start = datetime.datetime.now()
end = start + datetime.timedelta(minutes=25)
notification.notify(title="Pomodoro Technique Activated!",
                    message="Starting your 25min Work, Good luck",
                    app_icon="pngme.ico",
                    timeout=10
                    )
print(f"Starting Pomodoro Technique at {datetime.datetime.now().strftime('%H:%M:%S (%Y/%m/%d)')}")

while True:
    if datetime.datetime.now() > end:
        notification.notify(title="Please take a short Break",
                            message="You Have studied for 25 Minutes, Take 5min Breaks! (Pomodoro Technique)",
                            app_icon="pngme.ico",
                            timeout=15
                            )

        # sleep 5min (5x60=300)
        t_time = datetime.datetime.now()-total
        print(f"You have Studied for {str(t_time).split('.')[0]}")
        time.sleep(300)

        notification.notify(title="Get back to Work",
                            message="Start your 25min Work again, Good luck",
                            app_icon="pngme.ico",
                            timeout=10
                            )
        end = end + datetime.timedelta(minutes=25)
