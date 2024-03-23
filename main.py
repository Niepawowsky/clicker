from pynput import mouse, keyboard
from controller import Controller
from pprint import pprint
import json
from controller import Controller


class Process:
    def __init__(self, filename, controller):
        self.filename = filename
        self.steps = []
        self.controller = controller

    def load_steps(self):
        with open(self.filename) as file:
           self.steps = json.load(file)['steps']

    def start(self):
        for step in self.steps:
            print(step)
            # try:
            #     for steps in data["steps"]:
            #         print(steps["ControllerFunction1"].get("argument_name1a"))
            #         # for action in steps:
            #         #     print(type(action))
            #         # # for function in step:
            #         # #     print(function)
            #         # pprint(step["ControllerFunction1"]["argument_name1a"])


        # except KeyError:
        #     print('Nieprawidłowa nazwa funkcji')

        # for action in s:
        #     pprint(action)




def main():
    controller = Controller()
    process = Process('action_paint_line.json', controller)
    process.load_steps()
    process.start()

        # controller.type_button(keyboard.Key.cmd_l)
        # controller.type('paint')
        # controller.type_button(keyboard.Key.enter)
        #
        # controller.press_and_hold(keyboard.Key.cmd_l, keyboard.Key.up)
        #
        # controller.place_pointer(2272, 93)
        # controller.click_button(mouse.Button.left)
        # controller.place_pointer(2790, 133)
        # controller.click_button(mouse.Button.left)
        # controller.place_pointer(2790, 317)
        # controller.click_button(mouse.Button.left)
        # controller.place_pointer(2119, 499)
        # controller.single_mouse_action['hold_button'](mouse.Button.left)
        # controller.move_pointer(150,0)
        # controller.single_mouse_action['release_button'](mouse.Button.left)

main()