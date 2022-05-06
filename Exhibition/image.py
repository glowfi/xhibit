import os
from tcolorpy import tcolor
from Exhibition import color_palette
import getpass
import os


host = os.uname()[1]


def print_(info, field_colors, choice, img_path):
    username = "- " + getpass.getuser()
    img_path = img_path.split("/")[-1]
    choice["charac"] = f"{img_path}"
    ch = "Image:" + choice["charac"] + " "
    t = "Theme:" + choice["theme"]
    spc_ = "=" * len(ch + t + " ")
    spc = " " * 65
    k = len(info[9]) + len(host) + len(username) + len("ram : ")
    k1 = " " * (k - (len(host) + len(username)))
    username = k1 + username
    spc__ = "=" * k
    print(
        tcolor(f"{spc}                      ", color=field_colors[0], styles=["bold"])
    )
    print(
        tcolor(f" {spc}{ch}{t}              ", color=field_colors[4], styles=["bold"])
    )
    print(
        tcolor(f" {spc}{spc_}               ", color=field_colors[0], styles=["bold"])
    )
    print(tcolor(f"{spc} {info[0]}       ", color=field_colors[0], styles=["bold"]))
    print(tcolor(f"{spc} {info[1]}   ", color=field_colors[1], styles=["bold"]))
    print(tcolor(f"{spc} {info[2]} ", color=field_colors[2], styles=["bold"]))
    print(tcolor(f"{spc} {info[3]}    ", color=field_colors[3], styles=["bold"]))
    print(tcolor(f"{spc} {info[4]}    ", color=field_colors[4], styles=["bold"]))
    print(tcolor(f"{spc} {info[5]}   ", color=field_colors[5], styles=["bold"]))
    print(tcolor(f"{spc} {info[6]}      ", color=field_colors[6], styles=["bold"]))
    print(tcolor(f"{spc} {info[7]}      ", color=field_colors[2], styles=["bold"]))
    print(tcolor(f"{spc} {info[8]}      ", color=field_colors[5], styles=["bold"]))
    print(tcolor(f"{spc} {info[9]}      ", color=field_colors[4], styles=["bold"]))
    color_palette.color_test("image")
    print(
        tcolor(f"{spc}{spc__}               ", color=field_colors[4], styles=["bold"])
    )
    print(
        tcolor(f"{spc}{username}@{host}     ", color=field_colors[2], styles=["bold"])
    )


def display_image(image_path, info, field_colors, image_backend, cropMode, choice):

    # Print ascii first for ueberzug
    if image_backend == "ueberzug":
        print_(info, field_colors, choice, image_path)

    # Getting Path
    pos_loc = os.path.realpath(__file__)
    ind = str(pos_loc).find(".local")
    pos_loc = f"{pos_loc[0:ind-1]}/.local/bin/pos.sh"

    # Running Shell script
    call_with_args = f"{pos_loc} {image_path} {image_backend} {cropMode}"
    os.system(call_with_args)

    # Print ascii last for kitty
    if image_backend == "kitty":
        print_(info, field_colors, choice, image_path)

    # Put the cursor at the end of terminal's row
    call_with_args = "output=$(tput lines);tput cup $output 0"
    os.system(call_with_args)
