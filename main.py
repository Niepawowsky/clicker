from pynput import mouse, keyboard
from time import sleep
import ctypes

PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)


class Controller:
    wait = 0.5

    """
    Class that controls and implement given instructions
    """

    def __init__(self) -> None:
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.single_mouse_action = {
            'hold_button': lambda button: self.mouse.press(button),
            'release_button': lambda button: self.mouse.release(button)
        }
        # sleep(Controller.wait)

    """Keyboard"""
    def type_button(self, button):
        self.keyboard.press(button)
        self.keyboard.release(button)
        sleep(Controller.wait)

    def press_and_hold(self, hold_button, press_button):
        with self.keyboard.pressed(hold_button):
            self.keyboard.press(press_button)
            self.keyboard.release(press_button)
            # sleep(Controller.wait)

    def type(self, text):
        self.keyboard.type(text)
        sleep(Controller.wait)

    """Mouse"""
    def click_button(self, button):
        self.mouse.press(button)
        self.mouse.release(button)
        sleep(Controller.wait)

    def place_pointer(self, coordinate_x, coordinate_y):
        self.mouse.position = (coordinate_x, coordinate_y)
        sleep(Controller.wait)

    def move_pointer(self, distance_x, distance_y):
        self.mouse.move(distance_x, distance_y)
        sleep(Controller.wait)

    # def action(self, action):
    #     func = {
    #         'hold_button': lambda button: self.mouse.press(button),
    #         'release_button': lambda button: self.mouse.release(button)
    #     }
    #     return func

    def hold_button(self, button):
        self.mouse.press(button)
        sleep(Controller.wait)

    def release_button(self, button):
        self.mouse.release(button)
        sleep(Controller.wait)

def main():
    controller = Controller()
    controller.type_button(keyboard.Key.cmd_l)
    controller.type('paint')
    controller.type_button(keyboard.Key.enter)

    controller.press_and_hold(keyboard.Key.cmd_l, keyboard.Key.up)

    controller.place_pointer(2272, 93)
    controller.click_button(mouse.Button.left)
    controller.place_pointer(2790, 133)
    controller.click_button(mouse.Button.left)
    controller.place_pointer(2790, 317)
    controller.click_button(mouse.Button.left)
    controller.place_pointer(2119, 499)
    controller.single_mouse_action['hold_button'](mouse.Button.left)
    controller.move_pointer(150,0)
    controller.single_mouse_action['release_button'](mouse.Button.left)

main()