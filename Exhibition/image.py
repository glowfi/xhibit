import os
import subprocess
from tcolorpy import tcolor


def display_image(image_path, info, field_colors):
    # print(info)
    spc = " " * 52
    print(tcolor(f"{spc}                      ", color=field_colors[0], styles=["bold"]))
    print(tcolor(f"{spc}                      ", color=field_colors[1], styles=["bold"]))
    print(tcolor(f"{spc} os : {info[0]}       ", color=field_colors[0], styles=["bold"]))
    print(tcolor(f"{spc} kernel : {info[1]}   ", color=field_colors[1], styles=["bold"]))
    print(tcolor(f"{spc} packages : {info[2]} ", color=field_colors[2], styles=["bold"]))
    print(tcolor(f"{spc} shell : {info[3]}    ", color=field_colors[3], styles=["bold"]))
    print(tcolor(f"{spc} de/wm : {info[4]}    ", color=field_colors[4], styles=["bold"]))
    print(tcolor(f"{spc} uptime : {info[5]}   ", color=field_colors[5], styles=["bold"]))
    print(tcolor(f"{spc} cpu : {info[6]}      ", color=field_colors[6], styles=["bold"]))
    print(tcolor(f"{spc} gpu : {info[7]}      ", color=field_colors[7], styles=["bold"]))
    print(tcolor(f"{spc}                      ", color=field_colors[7], styles=["bold"]))
    print(tcolor(f"{spc}                      ", color=field_colors[6], styles=["bold"]))
    print(tcolor(f"{spc}                      ", color=field_colors[0], styles=["bold"]))
    print(tcolor(f"{spc}                      ", color=field_colors[1], styles=["bold"]))

    cmd = "xdpyinfo | grep -oP 'dimensions:\s+\K\S+'|cut -d'x' -f2"
    p = os.popen(cmd)
    res = int(p.read()) / 1.5

    resize = ["convert", f"{image_path}", "-resize", f"{res}", "new.png"]
    subprocess.run(resize, stdout=subprocess.PIPE)

    # Getting Path
    pos_loc = os.path.realpath(__file__)
    ind = str(pos_loc).find("Exhibition")
    pos_loc = f"{pos_loc[0:ind-1]}/Exhibition/pos.sh"

    # Running Shell script
    # cmd = ["sh", f"{pos_loc}"]
    # info = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
    # ypos = int(info) // 10
    xpos = 1
    ypos=1
    # print(xpos)

    cmd = [
        "kitty",
        "+kitten",
        "icat",
        "--align",
        "left",
        "--place",
        f"50x50@{xpos}x{ypos}",
        f"new.png",
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE)
