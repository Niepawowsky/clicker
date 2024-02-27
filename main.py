from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from time import sleep
import ctypes

PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)


class Controller:
    """
    Class that controlls and implement given instructions
    """
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

mouse.position = (26, 1062)
mouse.press(Button.left)
mouse.release(Button.left)

sleep(0.1)

keyboard.type('paint')
sleep(0.5)
keyboard.press(Key.enter)
sleep(0.5)
# keyboard.press(Key.cmd_l)
# keyboard.release(Key.cmd_l)
sleep(0.5)
with keyboard.pressed(Key.cmd_l):
    keyboard.press(Key.up)
    keyboard.release(Key.up)

sleep(0.5)
mouse.position = (2272, 93)
sleep(0.5)
mouse.press(Button.left)
mouse.release(Button.left)
sleep(0.5)
mouse.position = (2790, 133)
sleep(0.5)
mouse.press(Button.left)
mouse.release(Button.left)
sleep(0.5)
mouse.position = (2790, 317)
sleep(0.5)
mouse.press(Button.left)
mouse.release(Button.left)
sleep(0.5)
mouse.position = (2119, 499)
sleep(0.5)
mouse.press(Button.left)
for _ in range(250):
    mouse.move(1, 0)
    sleep(0.0001)
mouse.release(Button.left)

