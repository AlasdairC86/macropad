import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
import board
from digitalio import DigitalInOut, Direction, Pull

#board is wired with gpio high and other end of switch connected to ground




#initate keyboard
kbd = Keyboard(usb_hid.devices)

#set gpio pins for buttons
B0 = DigitalInOut(board.GP0)
B1 = DigitalInOut(board.GP1)
B2 = DigitalInOut(board.GP2)
B3 = DigitalInOut(board.GP3)
B4 = DigitalInOut(board.GP4)
B5 = DigitalInOut(board.GP5)
B6 = DigitalInOut(board.GP6)
B7 = DigitalInOut(board.GP7)
B8 = DigitalInOut(board.GP8)

gpio_pins = ( B0, B1, B2, B3, B4, B5, B6, B7, B8)

#setup buttons 
for pin in gpio_pins:
    pin.direction = Direction.INPUT
    pin.pull = Pull.UP

"""
button Layout:
6 | 3 | 0
7 | 4 | 1
8 | 5 | 2

"""

macros = {
    0: [Keycode.CONTROL, Keycode.F8],
    1: [Keycode.CONTROL, Keycode.F9],
    2: [Keycode.CONTROL, Keycode.F10], 
    3: [Keycode.LEFT_CONTROL, Keycode.A],
    4: [Keycode.LEFT_CONTROL, Keycode.C],
    5: [Keycode.LEFT_CONTROL, Keycode.V],
    6: [Keycode.LEFT_CONTROL, Keycode.F7],
    7: [Keycode.LEFT_CONTROL, Keycode.SPACE],
    8: [Keycode.LEFT_SHIFT, Keycode.ALT, Keycode.R]        
            }




while True:


    for button in enumerate(gpio_pins):
        if button[1].value == False:
            print(button[0], button[1].value)
            kbd.send(*macros[button[0]])
            time.sleep(0.2)
            kbd.release_all()
            print(*macros[button[0]])




    