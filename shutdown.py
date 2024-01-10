#Make sure to copy this code into code.py AFTER install the circuitpython firmware onto your Raspberry Pi Pico
#Make sure you have the correct library installed otherwise this code wont work :)
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import board
import usb_hid


# Initialize the keyboard and keyboard layout
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

def send_keyboard_input(keys):
    for key in keys:
        keyboard.press(key)
        time.sleep(0.025)  # You can adjust the delay as needed
        keyboard.release_all()
        time.sleep(0.025)  # Adjust the delay between key presses if necessary


keyboard.press(Keycode.GUI)
keyboard.press(Keycode.R)
keyboard.release_all()
time.sleep(0.5)
send_keyboard_input([
    Keycode.C,
    Keycode.M,
    Keycode.D,
    Keycode.ENTER])
time.sleep(1)
send_keyboard_input([
    Keycode.S,
    Keycode.H,
    Keycode.U,
    Keycode.T,
    Keycode.D,
    Keycode.O,
    Keycode.W,
    Keycode.N,
    Keycode.SPACEBAR,
    Keycode.FORWARD_SLASH,
    Keycode.S,
    Keycode.SPACEBAR,
    Keycode.FORWARD_SLASH,
    Keycode.T,
    Keycode.SPACEBAR,
    Keycode.ZERO,
    Keycode.ENTER])
