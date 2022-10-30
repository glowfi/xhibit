from __future__ import print_function


# https://gist.github.com/christian-oudard/220521/16f5ee5e3c54653846445dbedd67d30f2328d5a3
"""
Utilities for 256 color support in terminals.
Adapted from:
http://stackoverflow.com/questions/1403353/256-color-terminal-library-for-ruby
The color palette is indexed as follows:
0-15: System colors
    0  black         8  dark gray
    1  dark red      9  red
    2  dark green    10 green
    3  dark yellow   11 yellow
    4  dark blue     12 blue
    5  dark purple   13 purple
    6  dark cyan     14 cyan
    7  light gray    15 white
16-231: 6x6x6 Color Cube
    All combinations of red, green, and blue from 0 to 5.
232-255: Grayscale Ramp
    24 shades of gray, not including black and white.
"""


def rgb(red, green, blue):
    """
    Calculate the palette index of a color in the 6x6x6 color cube.
    The red, green and blue arguments may range from 0 to 5.
    """
    return 16 + (red * 36) + (green * 6) + blue


def gray(value):
    """
    Calculate the palette index of a color in the grayscale ramp.
    The value argument may range from 0 to 23.
    """
    return 232 + value


def set_color(fg=None, bg=None):
    """
    Print escape codes to set the terminal color.
    fg and bg are indices into the color palette for the foreground and
    background colors.
    """
    if fg:
        print("\x1b[38;5;%dm" % fg, end="")
    if bg:
        print("\x1b[48;5;%dm" % bg, end="")


def reset_color():
    """
    Reset terminal color to default.
    """
    print("\x1b[0m", end="")


def print_color(*args, **kwargs):
    """
    Print function, with extra arguments fg and bg to set colors.
    """
    fg = kwargs.pop("fg", None)
    bg = kwargs.pop("bg", None)
    set_color(fg, bg)
    print(*args, **kwargs)
    reset_color()


def color_test(args):
    # Print a test graphic showing all colors.
    if args != "ascii":
        spc = 67
        sp_ = " " * spc
        sp_ += "\tColor Test"
        print()
        print(sp_)
        print(" " * 67, end="")
    else:
        print("\n\tColor Test")
        print(" " * 2, end="")
    for c in range(8):
        print_color("   ", bg=c, end="")
    print()
    if args != "ascii":
        print(" " * 67, end="")
    else:
        print(" " * 2, end="")
    for c in range(8, 16):
        print_color("   ", bg=c, end="")
    print()
    print()
