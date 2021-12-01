import os
import subprocess
import platform


def get_kernel():
    return platform.release()


def get_def_shell():
    return os.environ.get("SHELL").split("/")[2]


def get_distro():
    os_ = (
        subprocess.run(
            ["uname -o"],
            stdout=subprocess.PIPE,
            shell=True,
        )
        .stdout.decode("utf-8")
        .lstrip()
        .rstrip()
    )
    if os_ == "Android":
        return "Android"

    command = 'source /etc/os-release && printf "%s\n" "${PRETTY_NAME}"'
    return (
        subprocess.run(
            [command],
            stdout=subprocess.PIPE,
            shell=True,
        )
        .stdout.decode("utf-8")
        .lstrip()
        .rstrip()
    )


def get_packages():
    command = 'which {xbps-install,apk,apt,pacman,nix,dnf,rpm,dpkg,emerge} 2>&1 | grep -v "^which" | sed "s_.*/__"'
    pack = (
        subprocess.run(
            [command],
            stdout=subprocess.PIPE,
            shell=True,
        )
        .stdout.decode("utf-8")
        .lstrip()
        .rstrip()
    )

    if pack == "xbps-install":
        return (
            subprocess.run(
                ["xbps-query -l | wc -l"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )

    elif pack == "apk":
        return (
            subprocess.run(
                ["apk search | wc -l"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )
    elif pack == "apt":
        return (
            subprocess.run(
                ["apt list --installed 2>/dev/null | wc -l"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )
    elif pack == "dnf":
        return (
            subprocess.run(
                ["dnf list installed | wc -l"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )
    elif pack == "nix":
        return (
            subprocess.run(
                ['nix-env -qa --installed "*" | wc -l'],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )
    elif pack == "pacman":
        return (
            subprocess.run(
                ["pacman -Q | wc -l"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )
    elif pack == "rpm":
        return (
            subprocess.run(
                ["rpm -qa | wc -l"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )
    elif pack == "emerge":
        return (
            subprocess.run(
                ["qlist -I | wc -l"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
        )
    else:
        return "Unknowm"


def get_init():
    os_ = (
        subprocess.run(
            ["uname -o"],
            stdout=subprocess.PIPE,
            shell=True,
        )
        .stdout.decode("utf-8")
        .lstrip()
        .rstrip()
    )
    check_sysD = (
        subprocess.run(
            ["pidof -q systemd"],
            stdout=subprocess.PIPE,
            shell=True,
        )
        .stdout.decode("utf-8")
        .lstrip()
        .rstrip()
    )

    if os_ == "Android":
        return "init.rc"
    elif not check_sysD:
        if os.path.exists("/sbin/openrc"):
            return "openrc"
        else:
            return (
                subprocess.run(
                    ["cat /proc/1/comm"],
                    stdout=subprocess.PIPE,
                    shell=True,
                )
                .stdout.decode("utf-8")
                .lstrip()
                .rstrip()
            )

    else:
        return "systemd"


def get_de_wm():
    de = os.environ.get("XDG_CURRENT_DESKTOP")
    wm = None

    if de:
        return de

    elif not de:
        # For most WMs
        get_id = (
            subprocess.run(
                ["xprop -root -notype _NET_SUPPORTING_WM_CHECK"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
            .split(" ")[-1]
        )
        command = f"xprop -id {get_id} -notype -len 100 -f _NET_WM_NAME 8t"
        wm = (
            subprocess.run(
                [f"{command}|grep '^_NET_WM_NAME'"],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
            .split(" ")[-1]
        )

        if wm:
            return wm[1:-1]

        # For non-EWMH WMs
        wm = (
            subprocess.run(
                [
                    'ps -e | grep -m 1 -o -e "sway" -e "kiwmi" -e "wayfire" -e "sowm" -e "catwm" -e "fvwm" -e "dwm" -e "2bwm" -e "monsterwm" -e "tinywm" -e "xmonad"'
                ],
                stdout=subprocess.PIPE,
                shell=True,
            )
            .stdout.decode("utf-8")
            .lstrip()
            .rstrip()
            .split(" ")[-1]
        )

        if wm:
            return wm

    elif not de and not wm:
        return "No DE/WM Running"


def get_uptime():
    seconds = float(
        subprocess.check_output(["cat", "/proc/uptime"]).decode("utf-8").split()[0]
    )

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


def get_cpu():
    cpu_ = (
        subprocess.run(
            [
                'lscpu | grep -e "Model name" -e "CPU max MHz" -e "CPU(s)" -m 4|cut -d ":" -f 2'
            ],
            stdout=subprocess.PIPE,
            shell=True,
        )
        .stdout.decode("utf-8")
        .lstrip()
        .rstrip()
        .split("\n")
    )
    del cpu_[1]

    cpu_ = [i.lstrip().rstrip() for i in cpu_]

    return (
        cpu_[1] + " " + cpu_[0] + " cores" + " @ " + str(float(cpu_[2]) // 1000) + "Ghz"
    )


def get_gpu():
    return (
        subprocess.run(
            ["lspci |grep VGA|cut -d ':' -f 3|xargs"],
            stdout=subprocess.PIPE,
            shell=True,
        )
        .stdout.decode("utf-8")
        .lstrip()
        .rstrip()
    )


# print(get_de_wm())
# print(get_init())
# print(get_package())
# print(get_distro())
# print(get_kernel())
# print(get_def_shell())
# print(get_uptime())
# print(get_cpu())
# print(get_gpu())
