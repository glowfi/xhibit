#!/bin/sh

# Get distro name
distroName() {
	kernel_name=$(uname -s)
	case $kernel_name in

	Linux | GNU*)
		os=Linux
		;;

	*)
		printf '%s\n' "Unknown OS detected: '$kernel_name', aborting..." >&2
		printf '%s\n' "Open an issue on GitHub to add support for your OS." >&2
		exit 1
		;;
	esac

	[[ $distro ]] && return

	case $os in
	Linux | BSD | MINIX)
		if [[ -f /bedrock/etc/bedrock-release && -z $BEDROCK_RESTRICT ]]; then
			case $distro_shorthand in
			on | tiny) distro="Bedrock Linux" ;;
			*) distro=$(</bedrock/etc/bedrock-release) ;;
			esac

		elif [[ -f /etc/redstar-release ]]; then
			case $distro_shorthand in
			on | tiny) distro="Red Star OS" ;;
			*) distro="Red Star OS $(awk -F'[^0-9*]' '$0=$2' /etc/redstar-release)" ;;
			esac

		elif [[ -f /etc/armbian-release ]]; then
			. /etc/armbian-release
			distro="Armbian $DISTRIBUTION_CODENAME (${VERSION:-})"

		elif [[ -f /etc/siduction-version ]]; then
			case $distro_shorthand in
			on | tiny) distro=Siduction ;;
			*) distro="Siduction ($(lsb_release -sic))" ;;
			esac

		elif [[ -f /etc/mcst_version ]]; then
			case $distro_shorthand in
			on | tiny) distro="OS Elbrus" ;;
			*) distro="OS Elbrus $(</etc/mcst_version)" ;;
			esac

		elif type -p pveversion >/dev/null; then
			case $distro_shorthand in
			on | tiny) distro="Proxmox VE" ;;
			*)
				distro=$(pveversion)
				distro=${distro#pve-manager/}
				distro="Proxmox VE ${distro%/*}"
				;;
			esac

		elif type -p lsb_release >/dev/null; then
			case $distro_shorthand in
			on) lsb_flags=-si ;;
			tiny) lsb_flags=-si ;;
			*) lsb_flags=-sd ;;
			esac
			distro=$(lsb_release "$lsb_flags")

		elif [[ -f /etc/os-release ||
			-f /usr/lib/os-release ||
			-f /etc/openwrt_release ||
			-f /etc/lsb-release ]]; then

			# Source the os-release file
			for file in /etc/lsb-release /usr/lib/os-release \
				/etc/os-release /etc/openwrt_release; do
				source "$file" && break
			done

			# Format the distro name.
			case $distro_shorthand in
			on) distro="${NAME:-${DISTRIB_ID}} ${VERSION_ID:-${DISTRIB_RELEASE}}" ;;
			tiny) distro="${NAME:-${DISTRIB_ID:-${TAILS_PRODUCT_NAME}}}" ;;
			off) distro="${PRETTY_NAME:-${DISTRIB_DESCRIPTION}} ${UBUNTU_CODENAME}" ;;
			esac

		elif [[ -f /etc/GoboLinuxVersion ]]; then
			case $distro_shorthand in
			on | tiny) distro=GoboLinux ;;
			*) distro="GoboLinux $(</etc/GoboLinuxVersion)" ;;
			esac

		elif [[ -f /etc/SDE-VERSION ]]; then
			distro="$(</etc/SDE-VERSION)"
			case $distro_shorthand in
			on | tiny) distro="${distro% *}" ;;
			esac

		elif type -p crux >/dev/null; then
			distro=$(crux)
			case $distro_shorthand in
			on) distro=${distro//version/} ;;
			tiny) distro=${distro//version*/} ;;
			esac

		elif type -p tazpkg >/dev/null; then
			distro="SliTaz $(</etc/slitaz-release)"

		elif type -p kpt >/dev/null &&
			type -p kpm >/dev/null; then
			distro=KSLinux

		elif [[ -d /system/app/ && -d /system/priv-app ]]; then
			distro="Android $(getprop ro.build.version.release)"

		# Chrome OS doesn't conform to the /etc/*-release standard.
		# While the file is a series of variables they can't be sourced
		# by the shell since the values aren't quoted.
		elif [[ -f /etc/lsb-release && $(</etc/lsb-release) == *CHROMEOS* ]]; then
			distro='Chrome OS'

		elif type -p guix >/dev/null; then
			case $distro_shorthand in
			on | tiny) distro="Guix System" ;;
			*) distro="Guix System $(guix -V | awk 'NR==1{printf $4}')" ;;
			esac

		# Display whether using '-current' or '-release' on OpenBSD.
		elif [[ $kernel_name = OpenBSD ]]; then
			read -ra kernel_info <<<"$(sysctl -n kern.version)"
			distro=${kernel_info[*]:0:2}

		else
			for release_file in /etc/*-release; do
				distro+=$(<"$release_file")
			done

			if [[ -z $distro ]]; then
				case $distro_shorthand in
				on | tiny) distro=$kernel_name ;;
				*) distro="$kernel_name $kernel_version" ;;
				esac

				distro=${distro/DragonFly/DragonFlyBSD}

				# Workarounds for some BSD based distros.
				[[ -f /etc/pcbsd-lang ]] && distro=PCBSD
				[[ -f /etc/trueos-lang ]] && distro=TrueOS
				[[ -f /etc/pacbsd-release ]] && distro=PacBSD
				[[ -f /etc/hbsd-update.conf ]] && distro=HardenedBSD
			fi
		fi

		if [[ $(</proc/version) == *Microsoft* || $kernel_version == *Microsoft* ]]; then
			windows_version=$(wmic.exe os get Version)
			windows_version=$(trim "${windows_version/Version/}")

			case $distro_shorthand in
			on) distro+=" [Windows $windows_version]" ;;
			tiny) distro="Windows ${windows_version::2}" ;;
			*) distro+=" on Windows $windows_version" ;;
			esac

		elif [[ $(</proc/version) == *chrome-bot* || -f /dev/cros_ec ]]; then
			[[ $distro != *Chrome* ]] &&
				case $distro_shorthand in
				on) distro+=" [Chrome OS]" ;;
				tiny) distro="Chrome OS" ;;
				*) distro+=" on Chrome OS" ;;
				esac
			distro=${distro## on }
		fi

		# distro=$(trim_quotes "$distro")
		distro=${distro/NAME=/}

		# Get Ubuntu flavor.
		if [[ $distro == "Ubuntu"* ]]; then
			case $XDG_CONFIG_DIRS in
			*"studio"*) distro=${distro/Ubuntu/Ubuntu Studio} ;;
			*"plasma"*) distro=${distro/Ubuntu/Kubuntu} ;;
			*"mate"*) distro=${distro/Ubuntu/Ubuntu MATE} ;;
			*"xubuntu"*) distro=${distro/Ubuntu/Xubuntu} ;;
			*"Lubuntu"*) distro=${distro/Ubuntu/Lubuntu} ;;
			*"budgie"*) distro=${distro/Ubuntu/Ubuntu Budgie} ;;
			*"cinnamon"*) distro=${distro/Ubuntu/Ubuntu Cinnamon} ;;
			esac
		fi
		;;

	esac

	distro=${distro//Enterprise Server/}

	[[ $distro ]] || distro="$os (Unknown)"
    dist=$(echo "$distro" | tr -d '"')

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
		total="$(xbps-query -l | wc -l) packages [xbps]"
		;;
	"apk")
		total="$(apk search | wc -l) packages [apk]"
		;;
	"apt")
		total="$(apt list --installed 2>/dev/null | wc -l) packages [apt]"
		;;
	"pacman")
		total="$(pacman -Q | wc -l) packages [pacman]"
		;;
	"nix")
		total="$(nix-env -qa --installed "*" | wc -l) packages [nix]"
		;;
	"dnf")
		total="$(dnf list installed | wc -l) packages [dnf]"
		;;
	"rpm")
		total="$(rpm -qa | wc -l) packages [rpm]"
		;;
	"emerge")
		total="$(qlist -I | wc -l) packages [emerge]"
		;;
	"dpkg")
		total="$(dpkg-query -l | wc -l) packages [dpkg]"
		;;
	"")
		total="Unknown"
		;;
	esac

	varPkg="$total"
}

# Get default shell
defaultShell() {
	shell=$(echo ${SHELL##*/})
}

# Get Storage info
storageInfo() {
	storage="$(df -h / | awk '/^\//{print $3"/"$2}')"
}

# Get Memory usage
memoryUsage() {
    free_output=$(free -h --si | grep Mem)
	MEMUSED=$(echo $free_output | awk '{print $3}')
	MEMTOT=$(echo $free_output | awk '{print $2}')

	mem=$(echo "$MEMUSED/$MEMTOT")
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

	speed="$(lscpu | grep -e "Model name" -e "CPU max MHz" -e "CPU(s)" -m 5 | tail -1 | cut -d ":" -f 2 | cut -d "." -f 1 | xargs)"
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
		gpu=$(echo "$gpu" | xargs)
        _gpu=$(echo -e "$_gpu 󰭯 $gpu")
	done

	return
}

trim() {
    set -f
    # shellcheck disable=2048,2086
    set -- $*
    printf '%s\n' "${*//[[:space:]]/}"
    set +f
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

echo "OS : $dist $arch [$varInit]"
echo "Kernel : $kernel"
echo "Packages : $varPkg"
echo "Shell : $shell"
echo "DE/WM : $varWm"
echo "Uptime : $uptime"
echo "CPU : $cpu"
echo "GPU : $_gpu"
echo "Storage : $storage"
echo "Memory : $mem"
