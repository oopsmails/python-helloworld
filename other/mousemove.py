import pynput
from pynput.mouse import Button, Controller

mouse = Controller()

print("Current position: " + str(mouse.position))

mouse.position = (10, 20)
mouse.move(20, -13)


# Click the left button
mouse.click(Button.left, 1)
# Click the right button
mouse.click(Button.right, 1)
# Click the middle button
mouse.click(Button.middle, 1)
# Double click the left button
mouse.click(Button.left, 2)
# Click the left button ten times
mouse.click(Button.left, 10)

mouse.press(Button.left)
mouse.release(Button.left)

# Scroll up two steps
mouse.scroll(0, 2)
# Scroll right five steps
mouse.scroll(5, 0)

