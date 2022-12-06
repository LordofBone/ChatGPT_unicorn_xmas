import unicornhathd
from time import sleep
from random import randint

# Initialize the UnicornHathd display
unicornhathd.rotation(0)
unicornhathd.brightness(0.75)

# Set the initial colors for the tree
tree_colors = [
    (0, 100, 0),  # dark green for the tree base
    (0, 200, 0),  # green for the tree trunk
    (255, 0, 0),  # red for the tree lights
    (255, 255, 0),  # yellow for the star on top
]

# Animate the tree
while True:
    # Update the tree colors
    tree_colors[2] = (randint(200, 255), 0, 0)  # change the tree lights to red
    tree_colors[3] = (randint(0, 255), randint(0, 255), randint(0, 255))  # change the star to a random color

    # Draw the tree on the UnicornHathd
    unicornhathd.clear()

    # Draw the tree base
    for i in range(5):
        for j in range(5):
            unicornhathd.set_pixel(i, 6, tree_colors[0][0], tree_colors[0][1], tree_colors[0][2])

    # Draw the tree trunk
    for i in range(3):
        unicornhathd.set_pixel(i + 1, 5, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
        unicornhathd.set_pixel(i + 1, 4, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
        unicornhathd.set_pixel(i + 1, 3, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])

    # Draw a pointed top for the tree
    unicornhathd.set_pixel(1, 2, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
    unicornhathd.set_pixel(3, 2, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])

    # Alternate between drawing and not drawing the tree lights
    if tree_colors[2][0] == 0 and tree_colors[2][1] == 0 and tree_colors[2][2] == 0:
        # Draw the tree lights
        for i in range(3):
            unicornhathd.set_pixel(i + 1, 2, tree_colors[2][0], tree_colors[2][1], tree_colors[2][2])
            unicornhathd.set_pixel(i + 1, 1, tree_colors[2][0], tree_colors[2][1], tree_colors[2][2])
    else:
        # Don't draw the tree lights
        for i in range(3):
            unicornhathd.set_pixel(i + 1, 2, 0, 0, 0)
            unicornhathd.set_pixel(i + 1, 1, 0, 0, 0)

    # Draw the bottom part of the star
    unicornhathd.set_pixel(1, 0, tree_colors[2][0], tree_colors[2][1], tree_colors[2][2])
    unicornhathd.set_pixel(3, 0, tree_colors[2][0], tree_colors[2][1], tree_colors[2][2])

    # # Draw additional branches on the tree
    for i in range(5):  # changed the range to 5 instead of 3
        unicornhathd.set_pixel(i, 2, tree_colors[2][0], tree_colors[2][1], tree_colors[2][2])
        unicornhathd.set_pixel(i, 3, tree_colors[2][0], tree_colors[2][1], tree_colors[2][2])

    unicornhathd.set_pixel(0, 3, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
    unicornhathd.set_pixel(4, 3, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
    unicornhathd.set_pixel(1, 2, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
    unicornhathd.set_pixel(3, 2, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
    unicornhathd.set_pixel(1, 1, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])
    unicornhathd.set_pixel(3, 1, tree_colors[1][0], tree_colors[1][1], tree_colors[1][2])

    # Draw the star on top
    unicornhathd.set_pixel(2, 0, tree_colors[3][0], tree_colors[3][1], tree_colors[3][2])

    unicornhathd.show()

    # Pause for a moment before updating the colors again
    sleep(0.25)
