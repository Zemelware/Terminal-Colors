#!/usr/bin/python3

BOLD = '\33[1m'
ITALIC = '\33[3m'
UNDERLINE = '\33[4m'
BLINK = '\33[5m'
INVERT = '\33[7m'

BLACK = '\33[30m'
GREY = '\33[90m'
RED = '\33[31m'
REDLIGHT = '\33[91m'
GREEN = '\33[32m'
GREENLIGHT = '\33[92m'
YELLOW = '\33[33m'
YELLOWLIGHT = '\33[93m'
BLUE = '\33[34m'
BLUELIGHT = '\33[94m'
PURPLE = '\33[35m'
PURPLELIGHT = '\33[95m'
CYAN = '\33[36m'
CYANLIGHT = '\33[96m'
WHITE = '\33[37m'
WHITELIGHT = '\33[97m'

BLACKBG = '\33[40m'
GREYBG = '\33[100m'
REDBG = '\33[41m'
REDBGLIGHT = '\33[101m'
GREENBG = '\33[42m'
GREENBGLIGHT = '\33[102m'
YELLOWBG = '\33[43m'
YELLOWBGLIGHT = '\33[103m'
BLUEBG = '\33[44m'
BLUEBGLIGHT = '\33[104m'
PURPLEBG = '\33[45m'
PURPLEBGLIGHT = '\33[105m'
CYANBG = '\33[46m'
CYANBGLIGHT = '\33[106m'
WHITEBG = '\33[47m'
WHITEBGLIGHT = '\33[107m'


def printColor(text, *styles):
    for style in styles:
        print(style, end="")

    END = '\33[0m'
    print(str(text) + END)


def inputColor(text, *styles):
    for style in styles:
        print(style, end="")

    END = '\33[0m'
    input(str(text) + END)
