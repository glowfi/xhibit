### XHIBIT

> **Exhibit your ASCII art and system specs**

<p align="center">
  <img src="https://raw.githubusercontent.com/glowfi/xhibit/main/image_support.png" />
</p>

### COMPATIBILITY

**Works on any linux based distro.**

### INSTALLATION

### Add Path

**Note : Important**

> Must add ~/.local/bin/ in the PATH Variable <br>

<b>POSIX based shell (bash,zsh,dash,....) </b>

<em>Change bashrc to your repective shell's rc</em>

```
echo 'export PATH=~/.local/bin:$PATH' >> $HOME/.bashrc
```

<b>Fish shell </b>

```
echo 'set PATH ~/.local/bin/ $PATH' >> $HOME/.config/fish/config.fish
```

### Install Python Package

```
pip install xhibit
```

### Dependencies

**For Ascii art only**

-   **python 3.5+**

**For Image display**

-   **kitty terminal** or **ueberzug**
-   xorg-xdpyinfo
-   xdotool
-   xorg-xprop
-   xorg-xwininfo

### How To Use

```
usage: xhibit [-h] [-v] [-lcs LCS] [-cs CS] [-rcs RCS] [-ccs CCS] [-cn CN] [-rcn RCN] [-cpu CPU] [-gpu GPU] [-img IMG] [-imb IMB] [-crop CROP]

options:
  -h, --help  show this help message and exit
  -v          Prints version.
  -lcs LCS    List all colorschemes available [Pass 'all' as argument like this -> xhibit -lcs 'all']
  -cs CS      Colorscheme to display.
  -rcs RCS    Randomize Colorschemes [t or f].
  -ccs CCS    Give custom colorschemem of 8 colors like this "#BF616A,#A3BE8C,#EBCB8B,#81A1C1,#B48EAD,#88C0D0,#E5E9F0,#B48EAD".
  -cn CN      Specify Character name [monalisa,egyptian,fairy,casper,dragon].
  -rcn RCN    Randomize Characters [t or f].
  -cpu CPU    Mention Cpu [Custom Cpu name].
  -gpu GPU    Mention Gpu [Custom Gpu name].
  -img IMG    Image path.
  -imb IMB    Mention Image backend [kitty or ueberzug].
  -crop CROP  Mention crop type [fit or fill].
```

### ASCII characters

**ASCII Characters available**

-   monalisa
-   egyptian
-   casper
-   fairy
-   dragon

**Colorscheme available**

-   **212 colorschemes present**
-   **See the commands below on how to list all colorschemes present.**

### Example commands

**To Choose gruvbox Colorscheme and casper**

```sh
xhibit -cs gruvbox -cn casper
```

![example2](casper.png)

**To Choose dracula Colorscheme and fairy**

```sh
xhibit -cs dracula -cn fairy
```

![example3](fairy.png)

**To randomize colorscheme and character**

```sh
xhibit -rcs t -rcn t
```

![example4](egyptian.png)

### Colorschemes

Check **[Colorscheme list](https://raw.githubusercontent.com/glowfi/xhibit-colorschemes/main/colorscheme.txt)**

> List all colorschemes available

```sh
xhibit -lcs 'all'
```

> Picking a colorscheme

```sh
xhibit -cs "Eighties.dark" -cn dragon
```

![example4](pick_colorscheme.png)

**To give custom user colors**

You can give custom user colors to xhibit to display text.
Must give all the 8 colors in hex format seperated by a comma just
as shown below.Nord Colorscheme colors are used below as example.

```sh
xhibit -ccs "#BF616A,#A3BE8C,#EBCB8B,#81A1C1,#B48EAD,#88C0D0,#E5E9F0,#B48EAD"
```

![example0](./custom_colorscheme.png)

### Displaying Images

### Install ueberzug guide

<em>The original ueberzug project has been abandoned by its original author.
But there are some people who are continuing its legacy.
You can install ueberzug by using the below commands.
I know projects like `ueberzugpp` exists but for now
my project supports only `kitty` and `ueberzug` backend
to display images.</em>

```sh
git clone https://github.com/ueber-devel/ueberzug;
cd ueberzug/
pip install .
cd ..
rm -rf ueberzug
```

**Image support with ueberzug or kitty terminal.**

```sh
xhibit -img "path/to/image/file" -imb "kitty"

                or

xhibit -img "path/to/image/file" -imb "ueberzug"

```

**Image crop fit or fill**

```sh
xhibit -img "path/to/image/file" -imb "kitty" -crop "fit"
xhibit -img "path/to/image/file" -imb "kitty" -crop "fill"

                or

xhibit -img "path/to/image/file" -imb "ueberzug" -crop "fit"
xhibit -img "path/to/image/file" -imb "ueberzug" -crop "fill"

```

## ![example1](image_support.png)
