import unicornhathd
from time import sleep
from random import randint

# Initialize the UnicornHathd display
unicornhathd.rotation(0)
unicornhathd.brightness(0.75)

# Set the initial colors for the tree
tree = [
    (0, 100, 0),    # green for the tree base
    (0, 255, 0),    # bright green for the tree trunk
    (255, 0, 0),    # red for the tree lights
    (255, 255, 0),  # yellow for the star on top
]

# Animate the tree
while True:
    # Update the tree colors
    tree[2] = (randint(0, 255), randint(0, 255), randint(0, 255))  # change the tree lights to a random color
    tree[3] = (randint(0, 255), randint(0, 255), randint(0, 255))  # change the star to a random color

    # Draw the tree on the UnicornHathd
    unicornhathd.clear()
    unicornhathd.set_pixel(1, 6, tree[0][0], tree[0][1], tree[0][2])
    unicornhathd.set_pixel(2, 6, tree[0][0], tree[0][1], tree[0][2])
    unicornhathd.set_pixel(3, 6, tree[0][0], tree[0][1], tree[0][2])
    unicornhathd.set_pixel(2, 5, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(2, 4, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(2, 3, tree[1][0], tree[1][1], tree[1][2])
    unicornhathd.set_pixel(1, 2, tree[2][0], tree[2][1], tree[2][2])
    unicornhathd.set_pixel(2, 2, tree[2][0], tree[2][1], tree[2][2])
    unicornhathd.set_pixel(3, 2, tree[2][0], tree[2][1], tree[2][2])
    unicornhathd.set_pixel(2, 1, tree[3][0], tree[3][1], tree[3][2])
    unicornhathd.show()

    # Pause for a moment before updating the colors again
    sleep(0.25)
