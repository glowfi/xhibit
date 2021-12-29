from tcolorpy import tcolor
import getpass
import os

host = os.uname()[1]
username = getpass.getuser()
username = "glowfi"
spc=""
spc_=""
ch=""
t=""

def modify(choice,info):
    global ch
    global t
    global spc
    global spc_
    global username
    ch="ASCII:"+choice["charac"] +" "
    t="Theme:"+choice["theme"]
    spc = "=" * len(ch + t + " ") 
    spc_="=" * len(info)

def dragon(info,field_colors,choice):
    modify(choice,info[9])
    print("")
    print(tcolor(f"           /           /     {ch}{t}              ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"          /' .,,,,  ./       {spc}                ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"         /';'     ,/         ◼ {info[0]}          ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"        / /   ,,//,`'`       ◼ {info[1]}          ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"       ( ,, '_,  ,,,' ``     ◼ {info[2]}          ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"       |    /@  ,,, ;'' `    ◼ {info[3]}          ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"      /    .   ,''/' `,``    ◼ {info[4]}          ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f"     /   .     ./, `,, ` ;   ◼ {info[5]}          ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f"  ,./  .   ,-,',` ,,/''\,'   ◼ {info[6]}          ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f" |   /; ./,,'`,,'' |   |     ◼ {info[7]}          ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f" |     /   ','    /    |     ◼ {info[8]}          ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"  \___/'   '     |     |     ◼ {info[9]}          ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"    `,,'  |      /     `\    {spc_}               ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"         /      |        \   {username}@{host}    ",color=field_colors[1],styles=["bold"]))
    print("")


def monalisa(info,field_colors,choice):
    modify(choice,info[9])
    print("")
    print(tcolor(f"           ____                                   ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"         o8%8888,                                 ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f"       o88%8888888.                               ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"      8'-    -:8888b                              ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"     8'         8888         {ch}{t}              ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"    d8.-=. ,==-.:888b        {spc}                ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"    >8 `~` :`~' d8888        m {info[0]}          ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"    88         ,88888        o {info[1]}          ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"    88b. `-~  ':88888        n {info[2]}          ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"    888b ~==~ .:88888        a {info[3]}          ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"    88888o--:':::8888        l {info[4]}          ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f"    `88888| :::' 8888b       i {info[5]}          ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f"    8888^^'       8888b      s {info[6]}          ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"   d888           ,%888b.    a {info[7]}          ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f"  d88%            %%%8--'-.  > {info[8]}          ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f" /88:.__ ,       _%-' ---  - < {info[9]}          ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"     '''::===..-'   =  --.  ` {spc_}              ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"                              {username}@{host}   ",color=field_colors[3],styles=["bold"]))
    print("")


def casper(info,field_colors,choice):
    modify(choice,info[9])
    print("")
    print(tcolor(f"     .-''''-.            {ch}{t}                  ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f"    / -   -  \           {spc}                    ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f"   |  .-. .- |           @ {info[0]}              ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"   |  \o| |o (           # {info[1]}              ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"   \     ^    \          % {info[2]}              ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"   |'.  )--'  /|         $ {info[3]}              ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"  / / '-. .-'`\ \        ! {info[4]}              ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f" / /'---` `---'\ \       ^ {info[5]}              ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f" '.__.       .__.'       & {info[6]}              ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"     `|     |`           ~ {info[7]}              ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f"      |     \            + {info[8]}              ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"      \      '--.        - {info[9]}              ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"       '.        `\      {spc_}                   ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"         `'---.   |      {username}@{host}        ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"            ,__) /                                ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"             `..'                                 ",color=field_colors[1],styles=["bold"]))
    print("")



def egyptian(info,field_colors,choice):
    modify(choice,info[9])
    print("")
    print(tcolor(f"             ?                                                               ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"         ____'_                   |   |                {ch}{t}               ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"        /'  _)))                  |\_/|______,         {spc}                 ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"       /===| _\                  /::| Q  ____)         𓅃 {info[0]}           ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"      ('___|   >   ,_           /:::|   /    ,_        𓃀 {info[1]}           ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"         o  _=    / _///       /::::|_ /    / _///     𓂀 {info[2]}           ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"   _______| |____/ |         _|:::::| |:___/ |         𓁖 {info[3]}           ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"  |  __)  \_/ /____|        | '----'\_/  /___|         𓉢 {info[4]}           ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f" _| / \    ) )             _| /  \   :  /              𓆘 {info[5]}           ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f"\__/   \    /             \__/    \    /               𓄀 {info[6]}           ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"       /   (                      /===(                𓀀 {info[7]}           ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f"      / \   \                    /     \               𓃔 {info[8]}           ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"     /   \   \                  /       \              𓃑 {info[9]}           ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"     |    \   \                 |        \             {spc_}                ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"     |     \   \                |         \            {username}@{host}     ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f"     |      \   \               |,_________\                                 ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"     |       \   \               /  )  / )                                   ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"     |,_______\___\             /  /  (  |                                   ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"       | /   \ |                | /    \ |                                   ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f"       |/     \|                |/      \|                                   ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"       S__     S__              S__      S__                                 ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f"      /___\   /___\            /___\    /___\                                ",color=field_colors[4],styles=["bold"]))
    print("")


def fairy(info,field_colors,choice):
    modify(choice,info[9])
    print("")
    print(tcolor(f"       .--.   _,                                       ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"   .--;    \ /(_                  {ch}{t}              ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f"  /    '.   |   '-._    . ' .     {spc}                ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f" |       \  \    ,-.)  -= * =-    * {info[0]}          ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"  \ /\_   '. \((` .(    '/. '     * {info[1]}          ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"   )\ /     \ )\  _/   _/         * {info[2]}          ",color=field_colors[1],styles=["bold"]))
    print(tcolor(f"  /  \ \   .-'   '--. /_\         * {info[3]}          ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f" |    \ \_.' ,       \/||         * {info[4]}          ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f" \     \_.-';,_) _)'\ \||         * {info[5]}          ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f"  '.       /`\   (   '._/         * {info[6]}          ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"    `\   .;  |  . '.              * {info[7]}          ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f"      ).'  )/|      \             * {info[8]}          ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f"      `    ` |  \|   |            * {info[9]}          ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"              \  |   |            {spc_}               ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"               '.|   |            {username}@{host}    ",color=field_colors[0],styles=["bold"]))
    print(tcolor(f"                  \  '\__                              ",color=field_colors[6],styles=["bold"]))
    print(tcolor(f"                   `-._  '. _                          ",color=field_colors[3],styles=["bold"]))
    print(tcolor(f"                      \`;-.` `._                       ",color=field_colors[2],styles=["bold"]))
    print(tcolor(f"                       \ \ `'-._\                      ",color=field_colors[4],styles=["bold"]))
    print(tcolor(f"                        \ |                            ",color=field_colors[5],styles=["bold"]))
    print(tcolor(f"                         \ )                           ",color=field_colors[7],styles=["bold"]))
    print(tcolor(f"                          \_\                          ",color=field_colors[6],styles=["bold"]))
    print("")
