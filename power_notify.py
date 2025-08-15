import psutil
import winsound
from winotify import Notification, audio
from PIL import Image, ImageDraw
import pystray


def create_image():
    img = Image.new('RGB', (64, 64), color=(255, 255, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([16, 16, 48, 48], fill=(0, 0, 0))
    return img


def check_power():
    battery = psutil.sensors_battery()
    if battery and not battery.power_plugged:
        alert()


def alert():
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    toast = Notification(
        app_id="Power Alert",
        title="⚠ Laptop Unplugged!",
        msg="Your laptop is running on battery.",
        duration="long"
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def on_exit(icon, item):
    icon.stop()


if __name__ == '__main__':
    menu = pystray.Menu(
        pystray.MenuItem("Exit", on_exit)
    )

    icon = pystray.Icon("Power Alert", create_image(), "Power Alert", menu)

    def setup(icon):
        check_power()
        icon.stop()

    icon.run(setup)
