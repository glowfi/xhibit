#!/usr/bin/python

# Module Imports
from tcolorpy import tcolor
import subprocess
import platform
import os
import re
import random
import argparse


class xhibit:
    """A utility to showff your ascii arts and sytem specs."""

    def __init__(self, *args):

        # Global default variables
        self.info = []
        self.cschemes=['gruvbox','dracula']
        self.field_colors = None

        # User variables
        self.user_colors = args[0]
        self.randomize_user_colors = args[1]
        self.character_name = args[2]
        self.randomize_characters = args[3]

    def colorscheme(self):

        # Colorschemes
        gruvbox = ["#fb4934","#b8bb26","#fabd2f","#83a598","#d3869b","#8ec07c","#fe8019","#d79921"]
        dracula = ["#f8f8f2","#8be9fd","#50fa7b","#ffb86c","#ff79c6","#bd93f9","#ff5555","#f1fa8c"]

        if self.randomize_user_colors == "t":
            self.field_colors=eval(random.choice(self.cschemes))

        else:
            self.field_colors=eval(self.user_colors)


    def specs(self):

        # OSNAME
        os_name = subprocess.check_output(["cat", "/etc/os-release"]).decode("utf-8")
        os_name = os_name.split("\n")[0]
        matches = re.findall(r"\"(.+?)\"", os_name)
        os_name = "".join(matches)
        self.info.append(os_name)

        # KERNEL
        kernel = platform.release()
        self.info.append(kernel)

        # TOTAL PACKAGES
        packages = subprocess.Popen(
            "pacman -Q | wc -l",
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        packages = int(packages.stdout.readlines(-1)[0])
        self.info.append(packages)

        # DEFAULT USER SHELL
        shell = os.environ.get("SHELL").split("/")[2]
        self.info.append(shell)

        # Desktop Environment/Window Manager
        de_wm = os.environ.get("XDG_CURRENT_DESKTOP")
        self.info.append(de_wm)

        # UPTIME
        uptime = float(
            subprocess.check_output(["cat", "/proc/uptime"]).decode("utf-8").split()[0]
        )

        def time_format(seconds):
            if seconds is not None:
                seconds = int(seconds)
                d = seconds // (3600 * 24)
                h = seconds // 3600 % 24
                m = seconds % 3600 // 60
                s = seconds % 3600 % 60
                if d > 0:
                    return "{:02d}D {:02d}h {:02d}m {:02d}s".format(d, h, m, s)
                elif h > 0:
                    return "{:02d}h {:02d}m {:02d}s".format(h, m, s)
                elif m > 0:
                    return "{:02d}m {:02d}s".format(m, s)
                elif s > 0:
                    return "{:02d}s".format(s)
            return "-"

        uptime = time_format(uptime)
        self.info.append(uptime)

        # CPU GPU
        cpu_gpu = (
            subprocess.check_output(["cat", "/proc/cpuinfo"])
            .decode("utf-8")
            .split("\n")[4]
            .split(":")[1]
            .lstrip()
            .split(" ")
        )
        cpu = " ".join(cpu_gpu[0:2])
        gpu = " ".join(cpu_gpu[6:])
        self.info.append(cpu)
        self.info.append(gpu)

    def ascii_art(self):
        def dragon():
            print("")
            print(tcolor(f"           /           /                          ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"          /' .,,,,  ./                            ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"         /';'     ,/         | {self.info[0]}     ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"        / /   ,,//,`'`       | {self.info[1]}     ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"       ( ,, '_,  ,,,' ``     | {self.info[2]}     ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"       |    /@  ,,, ;'' `    | {self.info[3]}     ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"      /    .   ,''/' `,``    | {self.info[4]}     ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f"     /   .     ./, `,, ` ;   | {self.info[5]}     ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f"  ,./  .   ,-,',` ,,/''\,'   | {self.info[6]}     ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f" |   /; ./,,'`,,'' |   |     | {self.info[7]}     ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f" |     /   ','    /    |                          ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"  \___/'   '     |     |                          ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"    `,,'  |      /     `\                         ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"         /      |        \                        ",color=self.field_colors[1],styles=["bold"]))
            print("")


        def monalisa():
            print("")
            print(tcolor(f"           ____                                   ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"         o8%8888,                                 ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f"       o88%8888888.                               ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"      8'-    -:8888b                              ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"     8'         8888                              ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"    d8.-=. ,==-.:888b                             ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"    >8 `~` :`~' d8888        m {self.info[0]}     ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"    88         ,88888        o {self.info[1]}     ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"    88b. `-~  ':88888        n {self.info[2]}     ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"    888b ~==~ .:88888        a {self.info[3]}     ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"    88888o--:':::8888        l {self.info[4]}     ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f"    `88888| :::' 8888b       i {self.info[5]}     ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f"    8888^^'       8888b      s {self.info[6]}     ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"   d888           ,%888b.    a {self.info[7]}     ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"  d88%            %%%8--'-.                       ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f" /88:.__ ,       _%-' ---  -                      ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"     '''::===..-'   =  --.  `                     ",color=self.field_colors[0],styles=["bold"]))
            print("")


        def casper():
            print("")
            print(tcolor(f"     .-''''-.                                     ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f"    / -   -  \                                    ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"   |  .-. .- |           @ {self.info[0]}         ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"   |  \o| |o (           # {self.info[1]}         ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"   \     ^    \          % {self.info[2]}         ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"   |'.  )--'  /|         $ {self.info[3]}         ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"  / / '-. .-'`\ \        ! {self.info[4]}         ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f" / /'---` `---'\ \       ^ {self.info[5]}         ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f" '.__.       .__.'       & {self.info[6]}         ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"     `|     |`           ~ {self.info[7]}         ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"      |     \                                     ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"      \      '--.                                 ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"       '.        `\                               ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"         `'---.   |                               ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"            ,__) /                                ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"             `..'                                 ",color=self.field_colors[1],styles=["bold"]))
            print("")



        def egyptian():
            print("")
            print(tcolor(f"                 ?                                                               ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"             ____'_                   |   |                                      ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"            /'  _)))                  |\_/|______,                               ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"           /===| _\                  /::| Q  ____)         𓅃   {self.info[0]}    ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"          ('___|   >   ,_           /:::|   /    ,_        𓃀   {self.info[1]}    ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"             o  _=    / _///       /::::|_ /    / _///     𓂀   {self.info[2]}    ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"       _______| |____/ |         _|:::::| |:___/ |         𓁖   {self.info[3]}    ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"      |  __)  \_/ /____|        | '----'\_/  /___|         𓉢   {self.info[4]}    ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f"     _| / \    ) )             _| /  \   :  /              𓆘   {self.info[5]}    ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f"    \__/   \    /             \__/    \    /               𓄀   {self.info[6]}    ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"           /   (                      /===(                𓀀   {self.info[7]}    ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"          / \   \                    /     \                                     ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"         /   \   \                  /       \                                    ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"         |    \   \                 |        \                                   ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"         |     \   \                |         \                                  ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f"         |      \   \               |,_________\                                 ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"         |       \   \               /  )  / )                                   ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"         |,_______\___\             /  /  (  |                                   ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"           | /   \ |                | /    \ |                                   ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"           |/     \|                |/      \|                                   ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"           S__     S__              S__      S__                                 ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f"          /___\   /___\            /___\    /___\                                ",color=self.field_colors[4],styles=["bold"]))
            print("")


        def fairy():
            print("")
            print(tcolor(f"       .--.   _,                                       ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"   .--;    \ /(_                                       ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f"  /    '.   |   '-._    . ' .                          ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f" |       \  \    ,-.)  -= * =-    * {self.info[2]}     ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"  \ /\_   '. \((` .(    '/. '     * {self.info[0]}     ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"   )\ /     \ )\  _/   _/         * {self.info[1]}     ",color=self.field_colors[1],styles=["bold"]))
            print(tcolor(f"  /  \ \   .-'   '--. /_\         * {self.info[3]}     ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f" |    \ \_.' ,       \/||         * {self.info[4]}     ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f" \     \_.-';,_) _)'\ \||         * {self.info[5]}     ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f"  '.       /`\   (   '._/         * {self.info[6]}     ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"    `\   .;  |  . '.              * {self.info[7]}     ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"      ).'  )/|      \                                  ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"      `    ` |  \|   |                                 ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"              \  |   |                                 ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"               '.|   |                                 ",color=self.field_colors[0],styles=["bold"]))
            print(tcolor(f"                  \  '\__                              ",color=self.field_colors[6],styles=["bold"]))
            print(tcolor(f"                   `-._  '. _                          ",color=self.field_colors[3],styles=["bold"]))
            print(tcolor(f"                      \`;-.` `._                       ",color=self.field_colors[2],styles=["bold"]))
            print(tcolor(f"                       \ \ `'-._\                      ",color=self.field_colors[4],styles=["bold"]))
            print(tcolor(f"                        \ |                            ",color=self.field_colors[5],styles=["bold"]))
            print(tcolor(f"                         \ )                           ",color=self.field_colors[7],styles=["bold"]))
            print(tcolor(f"                          \_\                          ",color=self.field_colors[6],styles=["bold"]))
            print("")



        if self.randomize_characters == "t":
            characters_names = ["dragon", "monalisa", "casper", "egyptian","fairy"]
            charac = random.choice(characters_names)
            eval(charac + "()")
            pass
        else:
            eval(self.character_name + "()")



parser = argparse.ArgumentParser()
parser.add_argument("-cs", type=str, default="gruvbox", help="Colorscheme to display.")
parser.add_argument("-rcs", type=str, default="f", help="Randomize Colorschemes.")
parser.add_argument("-cn", type=str, default="monalisa", help="Specify Character name.")
parser.add_argument("-rcn", type=str, default="f", help="Randomize Characters.")
args = parser.parse_args()

obj = xhibit(args.cs,args.rcs,args.cn,args.rcn)
obj.colorscheme()
obj.specs()
obj.ascii_art()
