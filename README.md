### XHIBIT

> **Exhibit your ASCII ART and system specs**

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

> Arguments available

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

> Characters available

-   monalisa
-   egyptian
-   casper
-   fairy
-   dragon

> Example commands

**Image support only on kitty terminal**

```
xhibit -img image_location
```

![example0](image_support.png)

> **To Choose gruvbox Colorscheme and casper**

```
xhibit -cs gruvbox -cn casper
```

![example1](casper.png)

> **To Choose dracula Colorscheme and fairy**

```
xhibit -cs dracula -cn fairy
```

![example1](fairy.png)

> **To randomize colorscheme and character**

```
xhibit -rcs t -rcn t
```

![example2](monalisa.png)
