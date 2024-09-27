"""
circuit python script for macro pad on Rpi Pico 
switches wired to GPIO 0-9
"""

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
import board
from digitalio import DigitalInOut, Direction, Pull

#board is wired with gpio high and other end of switch connected to ground

"""
button Layout:
7 | 4 | 1
8 | 5 | 2
9 | 6 | 3

"""


#initate keyboard
kbd = Keyboard(usb_hid.devices)

#set gpio pins for buttons
B1 = DigitalInOut(board.GP0)
B2 = DigitalInOut(board.GP1)
B3 = DigitalInOut(board.GP2)
B4 = DigitalInOut(board.GP3)
B5 = DigitalInOut(board.GP4)
B6 = DigitalInOut(board.GP5)
B7 = DigitalInOut(board.GP6)
B8 = DigitalInOut(board.GP7)
B9 = DigitalInOut(board.GP8)

gpio_pins = ( B1, B2, B3, B4, B5, B6, B7, B8, B9)

#setup buttons 
for pin in gpio_pins:
    pin.direction = Direction.INPUT
    pin.pull = Pull.UP


macros = ([Keycode.LEFT_CONTROL, Keycode.X],
            [Keycode.LEFT_CONTROL, Keycode.V], 
            [Keycode.LEFT_CONTROL, Keycode.A],
            [Keycode.LEFT_CONTROL, Keycode.Z],
            [Keycode.ALT, Keycode.LEFT_SHIFT, Keycode.R]         
            )



while True:


    for button in enumerate(gpio_pins):
        if button[1].value == False:
            print(button[0], button[1].value)
            kbd.send(*macros[button[0]])
            time.sleep(0.2)
            kbd.release_all()



    