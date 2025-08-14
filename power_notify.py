import time
import psutil
import winsound
from winotify import Notification, audio

def check_power():
    battery = psutil.sensors_battery()
    while battery and not battery.power_plugged:
        battery = psutil.sensors_battery()
        time.sleep(5)
        alert()

def alert():
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

    toast = Notification(
        app_id="Power Alert",
        title="⚠ Laptop Unplugged!",
        msg="Your laptop is running on battery.",
        duration="short"
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()

if __name__ == '__main__':
    check_power()
