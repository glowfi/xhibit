import os
import subprocess

# Getting Path
shell_loc = os.path.realpath(__file__)
ind = str(shell_loc).find("Exhibition")
shell_loc = f"{shell_loc[0:ind-1]}/Exhibition/shell.sh"

# Running Shell script
cmd = ["sh", f"{shell_loc}"]
info = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
info = str(info).split("\n")
info.pop()


def get_kernel():
    return info[1]


def get_def_shell():
    return info[3]


def get_distro():
    return info[0]


def get_packages():
    return info[2]


def get_de_wm():
    return info[4]


def get_uptime():
    return info[5]


def get_cpu():
    return info[6]


def get_gpu():
    return info[7]


def get_storage():
    return info[8]


def get_ram():
    return info[9]
