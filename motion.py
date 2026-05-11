from gpiozero import Button, MotionSensor
from picamera2 import Picamera2, Preview
from time import sleep
from signal import pause
# Import Path library for file paths
from pathlib import Path

# Connect button to GPIO pin 2
button = Button(2)
# Connect PIR motion sensor to GPIO pin 4
pir = MotionSensor(4)

# Create camera object
camera = Picamera2()
# Create preview configuration
preview_config = camera.create_preview_configuration()
# Apply camera configuration
camera.configure(preview_config)

# Start camera preview
camera.start_preview(Preview.QTGL)
camera.start()

# Wait 2 seconds for camera stabilization
sleep(2)

# Get home directory path
home = Path.home()

i = 0

# Function to stop the camera
def stop_camera():

    print("Camera stopped")
    camera.stop_preview()
    camera.stop()

    # Exit program
    raise SystemExit

# Function to capture photo
def take_photo():

    global i

    # Increase image counter
    i += 1
    # Create image file name
    filename = home / "Desktop" / f"image_{i}.jpg"
    # Capture and save image
    camera.capture_file(str(filename))

    print(f"Photographed : image_{i}.jpg")

    # Wait 10 seconds
    sleep(10)

# Stop camera when button is pressed
button.when_pressed = stop_camera

# Capture photo when motion is detected
pir.when_motion = take_photo

pause()