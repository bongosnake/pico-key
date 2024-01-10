#Make sure to copy this code into code.py AFTER install the circuitpython firmware onto your Raspberry Pi Pico
#Make sure you have the correct library installed otherwise this code wont work :)
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import board
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


consumer = ConsumerControl(usb_hid.devices)

# Initialize the keyboard and keyboard layout
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Function to send keyboard inputs
def send_keyboard_input(keys):
    for key in keys:
        keyboard.press(key)
        time.sleep(0.025)  # You can adjust the delay as needed
        keyboard.release_all()
        time.sleep(0.025)  # Adjust the delay between key presses if necessary

# Open Notepad (Win + R, "notepad", Enter)
keyboard.press(Keycode.GUI)
keyboard.press(Keycode.R)
time.sleep(1)  # Wait for the Run dialog to appear
keyboard.release_all()
send_keyboard_input([
    Keycode.C, 
    Keycode.H, 
    Keycode.R, 
    Keycode.O, 
    Keycode.M, 
    Keycode.E,
    Keycode.ENTER])  # Type "notepad" and press Enter
time.sleep(1)
keyboard.press(Keycode.CONTROL)
keyboard.press(Keycode.T)
time.sleep(0.5)
keyboard.release_all()
time.sleep(1)
#send_keyboard_input([
#   Keycode.H,
#  Keycode.T,
# Keycode.T,
# Keycode.P,
# Keycode.S,
#])
for _ in range(100):  # Adjust the number of iterations as needed
    consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
    time.sleep(0.00025)
#https://youtu.be/kG7d_4LeP48

#keyboard.press(Keycode.SHIFT)
#keyboard.press(Keycode.SEMICOLON)
#time.sleep(0.025)
#keyboard.release_all()
#time.sleep(0.025)
send_keyboard_input([
    Keycode.Y,
    Keycode.O,
    Keycode.U,
    Keycode.T,
    Keycode.U,
    Keycode.PERIOD,
    Keycode.B,
    Keycode.E,
    Keycode.FORWARD_SLASH,
    Keycode.K,
    Keycode.CAPS_LOCK,
    Keycode.G,
    Keycode.CAPS_LOCK,
    Keycode.SEVEN,
    Keycode.D])
keyboard.press(Keycode.SHIFT)
keyboard.press(Keycode.MINUS)
time.sleep(0.025)
keyboard.release_all()
time.sleep(0.025)
send_keyboard_input([
    Keycode.FOUR,
    Keycode.CAPS_LOCK,
    Keycode.L,
    Keycode.CAPS_LOCK,
    Keycode.E,
    Keycode.CAPS_LOCK,
    Keycode.P,
    Keycode.CAPS_LOCK,
    Keycode.FOUR,
    Keycode.EIGHT,
    Keycode.ENTER])