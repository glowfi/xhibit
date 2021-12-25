#!/bin/sh

# Get distro name
distroName() {
	os=$(uname -o)
	case ${os} in
	Android)
		distro="Android"
		;;
	*)
		distro=$(source /etc/os-release && printf '%s\n' "${PRETTY_NAME}")
		;;
	esac
}

# Get system architecture
distroArchitecture() {
	arch=$(uname -m)
}

# Get kernel name
kernelName() {
	kernel=$(uname -r)
}

# Get Init System
initSystem() {
	os=$(uname -o)
	if [[ $os = Android ]]; then
		varInit="init.rc"
	elif ! pidof -q systemd; then
		if [[ -f "/sbin/openrc" ]]; then
			varInit="openrc"
		else
			read -r varInit </proc/1/comm
		fi
	else
		varInit="systemD"
	fi
}

# Get Total Pacakges
pkgsTotal() {
	pack=$(which {xbps-install,apk,apt,pacman,nix,dnf,rpm,dpkg,emerge} 2>&1 | grep -v "^which" | sed 's_.*/__')
	case ${pack} in
	"xbps-install")
		total=$(xbps-query -l | wc -l)
		;;
	"apk")
		total=$(apk search | wc -l)
		;;
	"apt")
		total=$(apt list --installed 2>/dev/null | wc -l)
		;;
	"pacman")
		total=$(pacman -Q | wc -l)
		;;
	"nix")
		total=$(nix-env -qa --installed "*" | wc -l)
		;;
	"dnf")
		total=$(dnf list installed | wc -l)
		;;
	"rpm")
		total=$(rpm -qa | wc -l)
		;;
	"emerge")
		total=$(qlist -I | wc -l)
		;;
	"dpkg")
		total=$(dpkg-query -l | wc -l)
		;;
	"")
		total="Unknown"
		;;
	esac

	varPkg=$total
}

# Get default shell
defaultShell() {
	shell=$(echo ${SHELL##*/})
}

# Get Storage info
storageInfo() {
	IFS=, read storageavail storageused <<<"$(df -h / | awk '/^\//{print $2","$3}')"
}

# Get Memory usage
memoryUsage() {
	mem=$(free --mega | sed -n -E '2s/^[^0-9]*([0-9]+) *([0-9]+).*/'"${space}"'\2 \/ \1 MB/p')
}

# Get DE/WM
de_WM() {
	wm="${XDG_CURRENT_DESKTOP#*:}"
	[ "$wm" ] || wm="$DESKTOP_SESSION"

	# for most WMs
	[ ! "$wm" ] && [ "$DISPLAY" ] && command -v xprop >/dev/null && {
		id=$(xprop -root -notype _NET_SUPPORTING_WM_CHECK)
		id=${id##* }
		wm=$(xprop -id "$id" -notype -len 100 -f _NET_WM_NAME 8t | grep '^_NET_WM_NAME' | cut -d\" -f 2)
	}

	# for non-EWMH WMs
	[ ! "$wm" ] || [ "$wm" = "LG3D" ] &&
		wm=$(ps -e | grep -m 1 -o \
			-e "sway" \
			-e "kiwmi" \
			-e "wayfire" \
			-e "sowm" \
			-e "catwm" \
			-e "fvwm" \
			-e "dwm" \
			-e "2bwm" \
			-e "monsterwm" \
			-e "tinywm" \
			-e "xmonad")

	varWm=${wm:-unknown}
}

getUptime() {
	uptime=$(echo "$(uptime -p | sed 's/up//' | xargs)")
}

get_cpu() {
	cpu_file="/proc/cpuinfo"

	cpu="$(awk -F '\\s*: | @' \
		'/model name|Hardware|Processor|^cpu model|chip type|^cpu type/ {
                            cpu=$2; if ($1 == "Hardware") exit } END { print cpu }' "$cpu_file")"

	cpu="${cpu//(TM)/}"
	cpu="${cpu//(tm)/}"
	cpu="${cpu//(R)/}"
	cpu="${cpu//(r)/}"
	cpu="${cpu//CPU/}"
	cpu="${cpu//Processor/}"
	cpu="${cpu//Dual-Core/}"
	cpu="${cpu//Quad-Core/}"
	cpu="${cpu//Six-Core/}"
	cpu="${cpu//Eight-Core/}"
	cpu="${cpu//[1-9][0-9]-Core/}"
	cpu="${cpu//[0-9]-Core/}"
	cpu="${cpu//, * Compute Cores/}"
	cpu="${cpu//Core / }"
	cpu="${cpu//(\"AuthenticAMD\"*)/}"
	cpu="${cpu//with Radeon * Graphics/}"
	cpu="${cpu//with AMD Radeon * Graphics/}"
	cpu="${cpu//, altivec supported/}"
	cpu="${cpu//FPU*/}"
	cpu="${cpu//Chip Revision*/}"
	cpu="${cpu//Technologies, Inc/}"
	cpu="${cpu//Core2/Core 2}"

	cores=$(awk '/^core id/&&!a[$0]++{++i} END {print i}' "$cpu_file")
	cores="${cores//[[:space:]]/}"

	speed="$(lscpu | grep -e "Model name" -e "CPU max MHz" -e "CPU(s)" -m 4 | tail -1 | cut -d ":" -f 2 | cut -d "." -f 1 | xargs)"
	speed="${speed//[[:space:]]/}"

	if ((speed < 1000)); then
		cpu="$cpu($cores) @${speed}MHz"
		# cpu="$cpu($cores) cores"
	else
		[[ "$speed_shorthand" == "on" ]] && speed="$((speed / 100))"
		speed="${speed:0:1}.${speed:1}"
		cpu="$cpu($cores) @${speed}GHz"
		# cpu="$cpu($cores) cores"
	fi

}

get_gpu() {
	gpu_cmd="$(lspci -mm |
		awk -F '\"|\" \"|\\(' \
			'/"Display|"3D|"VGA/ {
                                  a[$0] = $1 " " $3 " " ($(NF-1) ~ /^$|^Device [[:xdigit:]]+$/ ? $4 : $(NF-1))
                              }
                              END { for (i in a) {
                                  if (!seen[a[i]]++) {
                                      sub("^[^ ]+ ", "", a[i]);
                                      print a[i]
                                  }
                              }}')"
	IFS=$'\n' read -d "" -ra gpus <<<"$gpu_cmd"

	[[ "${gpus[0]}" == *Intel* && "${gpus[1]}" == *Intel* ]] && unset -v "gpus[0]"

	for gpu in "${gpus[@]}"; do
		[[ "$gpu_type" == "dedicated" && "$gpu" == *Intel* ]] ||
			[[ "$gpu_type" == "integrated" && ! "$gpu" == *Intel* ]] &&
			{
				unset -v gpu
				continue
			}

		case $gpu in
		*"Advanced"*)
			brand="${gpu/*AMD*ATI*/AMD ATI}"
			brand="${brand:-${gpu/*AMD*/AMD}}"
			brand="${brand:-${gpu/*ATI*/ATi}}"

			gpu="${gpu/\[AMD\/ATI\] /}"
			gpu="${gpu/\[AMD\] /}"
			gpu="${gpu/OEM /}"
			gpu="${gpu/Advanced Micro Devices, Inc./}"
			gpu="${gpu/*\[/}"
			gpu="${gpu/\]*/}"
			gpu="$brand $gpu"
			;;

		*"NVIDIA"*)
			gpu="${gpu/*\[/}"
			gpu="${gpu/\]*/}"
			gpu="NVIDIA $gpu"
			;;

		*"Intel"*)
			gpu="${gpu/*Intel/Intel}"
			gpu="${gpu/\(R\)/}"
			gpu="${gpu/Corporation/}"
			gpu="${gpu/ \(*/}"
			gpu="${gpu/Integrated Graphics Controller/}"
			gpu="${gpu/*Xeon*/Intel HD Graphics}"

			[[ -z "$(trim "$gpu")" ]] && gpu="Intel Integrated Graphics"
			;;

		*"MCST"*)
			gpu="${gpu/*MCST*MGA2*/MCST MGA2}"
			;;

		*"VirtualBox"*)
			gpu="VirtualBox Graphics Adapter"
			;;

		*) continue ;;
		esac
	done

	return
}

distroName
distroArchitecture
initSystem
kernelName
pkgsTotal
defaultShell
storageInfo
memoryUsage
de_WM
getUptime
get_cpu
get_gpu

echo "$distro $arch [$varInit]"
echo "$kernel"
echo "$varPkg"
echo "$shell"
# echo "$storageavail / $storageused"
# echo "$mem"
echo "$varWm"
echo "$uptime"
echo "$cpu"
echo "$gpu"
