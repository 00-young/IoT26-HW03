from gpiozero import Button, MotionSensor
from picamera2 import Picamera2, Preview
from time import sleep
from signal import import pause
from pathlib import Path

button = Button(2)
pir = MotionSensor(4)

camera = Picamera2()

preview_config = camera.create_preview_configuration()

camera.configure(preview_config)

camera.start_preview(Preview.QTGL)

camera.start()

sleep(2)

home = Path.home()

i = 0

def stop_camera():

    print("Camera stopped")

    camera.stop_preview()
    camera.stop()

    raise SystemExit

def take_photo():

    global i

    i += 1

    filename = home / "Desktop" / f"image_{i}.jpg"

    camera.capture_file(str(filename))

    print(f"Photographed : image_{i}.jpg")

    sleep(10)

button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()
