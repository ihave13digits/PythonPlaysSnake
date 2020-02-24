#!/usr/bin/python3


import time

import os, sys

from os import O_NONBLOCK
from sys import stdin, exit
from termios import tcgetattr, ICANON, TCSANOW, ECHO, TCSAFLUSH, tcsetattr
from fcntl import fcntl, F_SETFL, F_GETFL

class Key:

    def __init__(self):
        self.esc = ""

class Keys:
    ARROW_UP: str = "\x1b[A"
    ARROW_DOWN: str = "\x1b[B"
    ARROW_RIGHT: str = "\x1b[C"
    ARROW_LEFT: str = "\x1b[D"
    ESC: str = "\x1b"
    ENTER: str = "\n"
    TAB: str = "\t"
    SPACE_BAR: str = " "


##-- Grabs Key --##


class Event():

    def keypress(keys_len=5):
        fd = stdin.fileno()

        oldterm = tcgetattr(fd)
        newattr = tcgetattr(fd)
        newattr[3] = newattr[3] & ~ICANON & ~ECHO
        tcsetattr(fd, TCSANOW, newattr)

        oldflags = fcntl(fd, F_GETFL)
        fcntl(fd, F_SETFL, oldflags | O_NONBLOCK)

        try:
            while True:
                try:
                    key = stdin.read(keys_len)
                    break
                except IOError:
                    pass
        finally:
            tcsetattr(fd, TCSAFLUSH, oldterm)
            fcntl(fd, F_SETFL, oldflags)
        return key

    def get_key(f=str):
        os.system("stty raw -echo")
        c = sys.stdin.read(1)
        os.system("stty -raw echo")
        return f(c)

    def get_text():
        txt = input()
        return txt
