# Module Imports
import random
import argparse
import sys
import os

from Exhibition import ascii
from Exhibition import sysinfo
from Exhibition import image


class xhibit:
    """A utility to showff your ascii arts and sytem specs."""

    def __init__(self, *args):

        # Global default variables
        self.info = []
        self.cschemes = ["gruvbox", "dracula"]
        self.field_colors = None
        self.cpu = args[4]
        self.gpu = args[5]
        self.image = args[6]

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
        self.info.append(sysinfo.get_distro())

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
        if not self.cpu:
            self.info.append(sysinfo.get_cpu())
        else:
            self.info.append(self.cpu)

        # GPU
        if not self.gpu:
            self.info.append(sysinfo.get_gpu())
        else:
            self.info.append(self.gpu)

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

    def disp_image(self):
        image.display_image(self.image, self.info, self.field_colors)


if __name__ == "Exhibition":
    pass
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-cs",
        type=str,
        default="gruvbox",
        help="Colorscheme to display [dracula,gruvbox].",
    )
    parser.add_argument(
        "-rcs", type=str, default="f", help="Randomize Colorschemes [t or f]."
    )
    parser.add_argument(
        "-cn",
        type=str,
        default="monalisa",
        help="Specify Character name [monalisa,egyptian,fairy,casper,dragon].",
    )
    parser.add_argument(
        "-rcn", type=str, default="f", help="Randomize Characters [t or f]."
    )
    parser.add_argument(
        "-cpu", type=str, default="", help="Mention Cpu [Custom Cpu name]."
    )
    parser.add_argument(
        "-gpu", type=str, default="", help="Mention Gpu [Custom Gpu name]."
    )
    parser.add_argument(
        "-img",
        type=str,
        default="",
        help="Image path [Image display works for kitty terminal only].",
    )
    args = parser.parse_args()

    if args.img != "":
        obj = xhibit(args.cs, args.rcs, args.cn, args.rcn, args.cpu, args.gpu, args.img)
        call_with_args = "reset"
        os.system(call_with_args)
        obj.colorscheme()
        obj.specs()
        obj.disp_image()
        sys.exit()
    else:
        obj = xhibit(args.cs, args.rcs, args.cn, args.rcn, args.cpu, args.gpu, args.img)
        obj.colorscheme()
        obj.specs()
        obj.ascii_art()
        sys.exit()
