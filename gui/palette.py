import curses


class Palette:

    NORMAL = 1
    HIGHLIGHTED = 2

    def __init__(self):
        curses.init_pair(self.NORMAL, 67, curses.COLOR_BLACK)
        curses.init_pair(self.HIGHLIGHTED, 255, curses.COLOR_BLACK)