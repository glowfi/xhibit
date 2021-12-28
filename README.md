### XHIBIT

> **Exhibit your ASCII art and system specs**

### INSTALLATION

```
pip install xhibit
```

### DEPENDENCIES

**For Ascii art only**

-   python 3.5+

**For Image display**

-   kitty
-   xorg-xdpyinfo
-   xdotool
-   xorg-xprop
-   xorg-xwininfo

### HOW TO USE

```
usage: xhibit [-h] [-cs CS] [-rcs RCS] [-ccs CCS] [-cn CN] [-rcn RCN] [-cpu CPU] [-gpu GPU] [-img IMG]

options:
  -h, --help  show this help message and exit
  -cs CS      Colorscheme to display [dracula,gruvbox].
  -rcs RCS    Randomize Colorschemes [t or f].
  -ccs CCS    Give custom colorschemem of 8 colors like this "#BF616A,#A3BE8C,#EBCB8B,#81A1C1,#B48EAD,#88C0D0,#E5E9F0,#B48EAD".
  -cn CN      Specify Character name [monalisa,egyptian,fairy,casper,dragon].
  -rcn RCN    Randomize Characters [t or f].
  -cpu CPU    Mention Cpu [Custom Cpu name].
  -gpu GPU    Mention Gpu [Custom Gpu name].
  -img IMG    Image path [Image display works for kitty terminal only].
```

**Characters available**

-   monalisa
-   egyptian
-   casper
-   fairy
-   dragon

**Available colorschemes**

-   gruvbox
-   dracula

> Example commands

**Image support only on kitty terminal**

```
xhibit -img image_location
```

![example1](image_support.png)

**To give custom user colors**

You can give custom user colors to xhibit to display text.
Must give all the 8 colors in hex format just as shown below.
Nord Colorscheme colors are used below as example.

```
xhibit -ccs "#BF616A,#A3BE8C,#EBCB8B,#81A1C1,#B48EAD,#88C0D0,#E5E9F0,#B48EAD"
```

![example0](./custom_colorscheme.png)

**To Choose gruvbox Colorscheme and casper**

```
xhibit -cs gruvbox -cn casper
```

![example2](casper.png)

**To Choose dracula Colorscheme and fairy**

```
xhibit -cs dracula -cn fairy
```

![example3](fairy.png)

**To randomize colorscheme and character**

```
xhibit -rcs t -rcn t
```

![example4](monalisa.png)
