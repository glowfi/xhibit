#!/bin/sh

wall="$1"
backend="$2"
crop_mode="$3"
crop_offset="center"

get_window_size() {

	# Get terminal width/height.
	if (("${term_width:-0}" < 50)) && [[ "$DISPLAY" && $os != "Mac OS X" && $os != "macOS" ]]; then
		if type -p xdotool &>/dev/null; then
			IFS=$'\n' read -d "" -ra win \
				<<<"$(xdotool getactivewindow getwindowgeometry --shell %1)"
			term_width="${win[3]/WIDTH=/}"
			term_height="${win[4]/HEIGHT=/}"

		elif type -p xwininfo &>/dev/null; then
			# Get the focused window's ID.
			if type -p xdo &>/dev/null; then
				current_window="$(xdo id)"

			elif type -p xprop &>/dev/null; then
				current_window="$(xprop -root _NET_ACTIVE_WINDOW)"
				current_window="${current_window##* }"

			elif type -p xdpyinfo &>/dev/null; then
				current_window="$(xdpyinfo | grep -F "focus:")"
				current_window="${current_window/*window /}"
				current_window="${current_window/,*/}"
			fi

			# If the ID was found get the window size.
			if [[ "$current_window" ]]; then
				term_size=("$(xwininfo -id "$current_window")")
				term_width="${term_size[0]#*Width: }"
				term_width="${term_width/$'\n'*/}"
				term_height="${term_size[0]/*Height: /}"
				term_height="${term_height/$'\n'*/}"
			fi
		fi
	fi

	term_width="${term_width:-0}"
}
get_window_size

get_term_size() {
	# Get the terminal size in cells.
	read -r lines columns <<<"$(stty size)"

	# Calculate font size.
	font_width="$((term_width / columns))"
	font_height="$((term_height / lines))"
}

get_term_size
# echo "$font_width"
# echo "$font_height"

get_image_size() {
	# This functions determines the size to make the thumbnail image.
	get_term_size
	image_size="auto"

	case $image_size in
	"auto")
		image_size="$((columns * font_width / 2))"
		term_height="$((term_height - term_height / 4))"

		((term_height < image_size)) &&
			image_size="$term_height"
		;;

	*"%")
		percent="${image_size/\%/}"
		image_size="$((percent * term_width / 100))"

		(((percent * term_height / 50) < image_size)) &&
			image_size="$((percent * term_height / 100))"
		;;

	"none")
		# Get image size so that we can do a better crop.
		read -r width height <<<"$(identify -format "%w %h" "$image")"

		while ((width >= (term_width / 2) || height >= term_height)); do
			((width = width / 2, height = height / 2))
		done

		crop_mode="none"
		;;

	*) image_size="${image_size/px/}" ;;
	esac

	# Check for terminal padding.
	[[ "$image_backend" == "w3m" ]] && term_padding

	width="${width:-$image_size}"
	height="${height:-$image_size}"
	text_padding="$(((width + padding + xoffset) / font_width + gap))"
}

get_image_size

make_thumbnail() {

	# Create cache directory if does not exists
	mkdir -p ~/.cache

	[[ -z "$size" ]] && {
		read -r og_width og_height <<<"$(identify -format "%w %h" "$wall")"
		((og_height > og_width)) && size="$og_width" || size="$og_height"
	}

	case $crop_mode in
	"fit")
		convert \
			-background none \
			"$wall" \
			-trim +repage \
			-gravity south \
			-extent "${size}x${size}" \
			-scale "${width}x${height}" \
			~/.cache/new.png
		;;

	"fill")
		convert \
			-background none \
			"$wall" \
			-trim +repage \
			-scale "${width}x${height}^" \
			-extent "${width}x${height}" \
			~/.cache/new.png
		;;

	*)
		convert \
			-background none \
			"$wall" \
			-strip \
			-gravity "$crop_offset" \
			-crop "${size}x${size}+0+0" \
			-scale "${width}x${height}" \
			~/.cache/new.png
		;;
	esac
}

make_thumbnail

if [[ "$backend" = "ueberzug" ]]; then
	setsid ueberzug layer --parser bash 0< <(
		declare -Ap add_command=([action]="add" [identifier]="example0" [x]="0" [y]="0" [path]=~/.cache/new.png
		)
		read -rs
	)
elif [[ "$backend" = "kitty" ]]; then

	kitty +kitten icat \
		--align left \
		--place "$((width / font_width))x$((height / font_height))@0x0" \
		~/.cache/new.png
else
	echo "No Image Backend Provided! Use Ueberzug or kitty terminal"
fi
