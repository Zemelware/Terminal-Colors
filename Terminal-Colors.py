#!/usr/bin/python3

END = '\33[0m'
BOLD = '\33[1m'
ITALIC = '\33[3m'
UNDERLINE = '\33[4m'
BLINK = '\33[5m'
INVERT = '\33[7m'

BLACK = '\33[30m'
GREY = '\33[90m'
RED = '\33[31m'
RED2 = '\33[91m'
GREEN = '\33[32m'
GREEN2 = '\33[92m'
YELLOW = '\33[33m'
YELLOW2 = '\33[93m'
BLUE = '\33[34m'
BLUE2 = '\33[94m'
PURPLE = '\33[35m'
PURPLE2 = '\33[95m'
BEIGE = '\33[36m'
BEIGE2 = '\33[96m'
WHITE = '\33[37m'
WHITE2 = '\33[97m'

BLACKBG = '\33[40m'
GREYBG = '\33[100m'
REDBG = '\33[41m'
REDBG2 = '\33[101m'
GREENBG = '\33[42m'
GREENBG2 = '\33[102m'
YELLOWBG = '\33[43m'
YELLOWBG2 = '\33[103m'
BLUEBG = '\33[44m'
BLUEBG2 = '\33[104m'
VIOLETBG = '\33[45m'
VIOLETBG2 = '\33[105m'
BEIGEBG = '\33[46m'
BEIGEBG2 = '\33[106m'
WHITEBG = '\33[47m'
WHITEBG2 = '\33[107m'


def printColor(text, *styles):
    for i in styles:
        print(i, end="")
    print(text + END)
