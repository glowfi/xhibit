#!/usr/bin/python

# Module Imports
import random
import argparse
import ascii
import sysinfo


class xhibit:
    """A utility to showff your ascii arts and sytem specs."""

    def __init__(self, *args):

        # Global default variables
        self.info = []
        self.cschemes = ["gruvbox", "dracula"]
        self.field_colors = None

        # User variables
        self.user_colors = args[0]
        self.randomize_user_colors = args[1]
        self.character_name = args[2]
        self.randomize_characters = args[3]

    def colorscheme(self):

        # Colorschemes
        gruvbox = [
            "#fb4934",
            "#b8bb26",
            "#fabd2f",
            "#83a598",
            "#d3869b",
            "#8ec07c",
            "#fe8019",
            "#d79921",
        ]
        dracula = [
            "#f8f8f2",
            "#8be9fd",
            "#50fa7b",
            "#ffb86c",
            "#ff79c6",
            "#bd93f9",
            "#ff5555",
            "#f1fa8c",
        ]

        if self.randomize_user_colors == "t":
            self.field_colors = eval(random.choice(self.cschemes))

        else:
            self.field_colors = eval(self.user_colors)

    def specs(self):

        # OSNAME
        self.info.append(sysinfo.get_distro() + f" [{sysinfo.get_init()}]")

        # KERNEL
        self.info.append(sysinfo.get_kernel())

        # TOTAL PACKAGES
        self.info.append(sysinfo.get_packages() + " packages")

        # DEFAULT USER SHELL
        self.info.append(sysinfo.get_def_shell())

        # Desktop Environment/Window Manager
        self.info.append(sysinfo.get_de_wm())

        # UPTIME
        self.info.append(sysinfo.get_uptime())

        # CPU
        self.info.append(sysinfo.get_cpu())

        # GPU
        self.info.append(sysinfo.get_gpu())

    def ascii_art(self):

        # Reading ASCII characters
        dragon = ascii.dragon
        monalisa = ascii.monalisa
        casper = ascii.casper
        egyptian = ascii.egyptian
        fairy = ascii.fairy

        if self.randomize_characters == "t":
            characters_names = ["dragon", "monalisa", "casper", "egyptian", "fairy"]
            charac = random.choice(characters_names)
            eval(f"{charac}")(self.info, self.field_colors)
        else:
            eval(f"{self.character_name}")(self.info, self.field_colors)


parser = argparse.ArgumentParser()
parser.add_argument("-cs", type=str, default="gruvbox", help="Colorscheme to display.")
parser.add_argument("-rcs", type=str, default="f", help="Randomize Colorschemes.")
parser.add_argument("-cn", type=str, default="monalisa", help="Specify Character name.")
parser.add_argument("-rcn", type=str, default="f", help="Randomize Characters.")
args = parser.parse_args()

obj = xhibit(args.cs, args.rcs, args.cn, args.rcn)
obj.colorscheme()
obj.specs()
obj.ascii_art()
