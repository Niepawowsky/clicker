"""
Script that will give you info about coordinates of your mouse pointer
"""
from pynput import mouse, keyboard



def on_click(x, y, button, pressed):
    click = f'x - {x} , y - {y}'
    print(click)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

with mouse.Listener(on_click=on_click), keyboard.Listener(on_press=on_press) as listener:
    listener.join()

