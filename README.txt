Hello there!
In order to turn your Raspberry Pi Pico into a keyboard emulator, you need to follow these steps first:
Download the circuit python uf2 image from this link: https://circuitpython.org/board/raspberry_pi_pico/
Plug your Pico into your PC
When plugged in, it should show up as "RPI-RP2". If not, hold down the BOOTSEL button located on the board whilst plugging the Pico in.
Drag and drop the circuitpython ufi into the Pico, which should be recognised as a storage device.
The Pico should dissapear and a new device called CIRCUITPY should appear.
You then need to download the HID library. To do this download the circuitpython library bundle from this link: https://circuitpython.org/libraries
Make sure to download the library compatible with your version of circuitpython
Extract the file onto you computer.
After this, locate the "lib" folder, and inside should be a folder called "adafruit_hid".
Drag and drop this into the "lib" folder located on the CIRCUITPY device.

This completes the dependancies you need!
From here you can code your own keyboard or mouse emulators!
After saving, unless you have made any changes to the board, it should automatically run the code saved in code.py.
The file containing your code MUST be called code.py, else it will not run.

The documentation for the adafruit_hid library is located here: https://docs.circuitpython.org/projects/hid/en/latest/

Now, whenever you plug your pico into a (windows) computer, the code you wrote will automatically run!
Enjoy!

(The links to the firmware and library are listed here, but are also kept inside this github repo for easy access. They will be kept up to date for as long as possible)
