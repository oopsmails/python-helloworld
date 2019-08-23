import time

from pynput.mouse import Button, Controller

mouse = Controller()

while True:
    # mouse.position = (300, 300)
    mouse.click(Button.right, 1)
    time.sleep(40)
    # mouse.position = (300, 350)
    # mouse.click(Button.right, 1)
    # time.sleep(8)
