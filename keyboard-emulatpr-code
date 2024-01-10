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
send_keyboard_input([Keycode.N, 
                     Keycode.O, 
                     Keycode.T, 
                     Keycode.E, 
                     Keycode.P, 
                     Keycode.A, 
                     Keycode.D,
                     Keycode.ENTER])  # Type "notepad" and press Enter

# Type "you smell" in Notepad
time.sleep(1)  # Wait for Notepad to open
send_keyboard_input([
    Keycode.Y,
    Keycode.O,
    Keycode.U,
    Keycode.SPACEBAR,
    Keycode.S,
    Keycode.M,
    Keycode.E,
    Keycode.L,
    Keycode.L
])


# Add more key sequences as needed
