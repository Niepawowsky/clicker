from pynput import mouse, keyboard
from time import sleep
import ctypes

# PROCESS_PER_MONITOR_DPI_AWARE = 2
# ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)


class Controller:
    wait = 0.5
    """
    Class that controls and implement given instructions
    """

    def __init__(self) -> None:
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        # sleep(Controller.wait)

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

    def click_button(self, button):
        self.mouse.press(button)
        self.mouse.release(button)
        sleep(Controller.wait)

    def place_pointer(self, coordinate_x, coordinate_y):
        self.mouse.position = (coordinate_x, coordinate_y)
        sleep(Controller.wait)

    def move_pointer(self, coordinate_x, coordinate_y):
        self.mouse.move(coordinate_x,coordinate_y)
        sleep(Controller.wait)

def main():
    controller = Controller()
    controller.type_button(keyboard.Key.cmd_l)
    controller.type('paint')
    controller.type_button(keyboard.Key.enter)

    controller.press_and_hold(keyboard.Key.cmd_l, keyboard.Key.up)

    controller.position = (2272, 93)
    controller.click_button(mouse.Button.left)
    controller.position = (2790, 133)
    controller.click_button(mouse.Button.left)
    controller.position = (2790, 317)
    controller.click_button(mouse.Button.left)
    controller.position = (2119, 499)
    controller.click_button(mouse.Button.left)
    # for _ in range(250):
    #     self.mouse.move(1, 0)
    #     sleep(0.0001)
    # self.mouse.release(mouse.Button.left)
main()