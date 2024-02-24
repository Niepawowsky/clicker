"""
Script that will give you info about coordinates of your mouse pointer
"""
from pynput import mouse


def on_click(x, y, button, pressed):
    print(f'x - {x} , y - {y}')

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
