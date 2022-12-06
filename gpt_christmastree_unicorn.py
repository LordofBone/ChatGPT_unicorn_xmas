import unicornhathd
from time import sleep
from random import randint

# Initialize the UnicornHathd display
unicornhathd.rotation(0)
unicornhathd.brightness(0.75)

# Set the initial colors for the tree
tree = [
    (0, 100, 0),  # green for the tree base
    (0, 255, 0),  # bright green for the tree trunk
    (255, 0, 0),  # red for the tree lights
    (255, 255, 0),  # yellow for the star on top
]

# Animate the tree
while True:
    # Update the tree colors
    tree[2] = (randint(0, 255), randint(0, 255), randint(0, 255))  # change the tree lights to a random color
    tree[3] = (randint(0, 255), randint(0, 255), randint(0, 255))  # change the star to a random color

    # Draw the tree on the UnicornHathd
    unicornhathd.clear()

    # Draw the tree base
    for i in range(5):
        for j in range(5):
            unicornhathd.set_pixel(i, 6, tree[0][0], tree[0][1], tree[0][2])

    # Draw the tree trunk
    for i in range(3):
        unicornhathd.set_pixel(i + 1, 5, tree[1][0], tree[1][1], tree[1][2])
        unicornhathd.set_pixel(i + 1, 4, tree[1][0], tree[1][1], tree[1][2])
        unicornhathd.set_pixel(i + 1, 3, tree[1][0], tree[1][1], tree[1][2])

    # Alternate between drawing and not drawing the tree lights
    if tree[2][0] == 0 and tree[2][1] == 0 and tree[2][2] == 0:
        # Draw the tree lights
        for i in range(3):
            unicornhathd.set_pixel(i + 1, 2, tree[2][0], tree[2][1], tree[2][2])
            unicornhathd.set_pixel(i + 1, 1, tree[2][0], tree[2][1], tree[2][2])
    else:
        # Don't draw the tree lights
        for i in range(3):
            unicornhathd.set_pixel(i + 1, 2, 0, 0, 0)
            unicornhathd.set_pixel(i + 1, 1, 0, 0, 0)

    # Draw the bottom part of the star
    unicornhathd.set_pixel(1, 0, tree[2][0], tree[2][1], tree[2][2])
    unicornhathd.set_pixel(3, 0, tree[2][0], tree[2][1], tree[2][2])

    # Draw additional branches on the tree
    for i in range(3):
        unicornhathd.set_pixel(i + 1, 2, tree[2][0], tree[2][1], tree[2][2])
        unicornhathd.set_pixel(i + 1, 3, tree[2][0], tree[2][1], tree[2][2])

    unicornhathd.set_pixel(0, 3, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(4, 3, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(1, 2, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(3, 2, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(1, 1, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(3, 1, tree[1][0], tree[1][1], tree[1][2])

    # Draw the star on top
    unicornhathd.set_pixel(2, 0, tree[3][0], tree[3][1], tree[3][2])

    unicornhathd.show()

    # Pause for a moment before updating the colors again
    sleep(0.25)
