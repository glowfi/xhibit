import os
from tcolorpy import tcolor
from Exhibition import color_palette


def display_image(image_path, info, field_colors):

    # Getting Path
    pos_loc = os.path.realpath(__file__)
    ind = str(pos_loc).find("Exhibition")
    pos_loc = f"{pos_loc[0:ind-1]}/Exhibition/pos.sh"

    # Running Shell script
    call_with_args = f"{pos_loc} {image_path}"
    os.system(call_with_args)

    # Print Ascii
    spc = " " * 55
    print(
        tcolor(f"{spc}                      ", color=field_colors[0], styles=["bold"])
    )
    print(
        tcolor(f"{spc} os : {info[0]}       ", color=field_colors[0], styles=["bold"])
    )
    print(
        tcolor(f"{spc} kernel : {info[1]}   ", color=field_colors[1], styles=["bold"])
    )
    print(
        tcolor(f"{spc} packages : {info[2]} ", color=field_colors[2], styles=["bold"])
    )
    print(
        tcolor(f"{spc} shell : {info[3]}    ", color=field_colors[3], styles=["bold"])
    )
    print(
        tcolor(f"{spc} de/wm : {info[4]}    ", color=field_colors[4], styles=["bold"])
    )
    print(
        tcolor(f"{spc} uptime : {info[5]}   ", color=field_colors[5], styles=["bold"])
    )
    print(
        tcolor(f"{spc} cpu : {info[6]}      ", color=field_colors[6], styles=["bold"])
    )
    print(
        tcolor(f"{spc} gpu : {info[7]}      ", color=field_colors[2], styles=["bold"])
    )
    print(
        tcolor(
            f"{spc} storage : {info[8]}      ", color=field_colors[5], styles=["bold"]
        )
    )
    print(
        tcolor(f"{spc} ram : {info[9]}      ", color=field_colors[4], styles=["bold"])
    )
    color_palette.color_test("image")

    # Put the cursor at the end of terminal's row
    call_with_args = "output=$(tput lines);tput cup $output 0"
    os.system(call_with_args)
