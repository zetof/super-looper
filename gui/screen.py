import curses
import atexit
from time import sleep

class Screen:

    def __init__(self):
        self.screen = curses.initscr()
        if not curses.has_colors():
            self.screen.addstr("Application should be run in a 256 colors capable terminal !!!")
            self.screen.refresh()
            sleep(5)
            self.destroy()
            exit(1)
        self.screen.keypad(True)
        self.screen.nodelay(True)
        self.height, self.width = self.screen.getmaxyx()
        curses.noecho()
        curses.curs_set(0)
        curses.cbreak()
        curses.start_color()
        atexit.register(self.destroy)

    def init_pair(self, index, color1, color2):
        curses.init_pair(index, color1, color2)

    def print_at(self, x, y, phrase, color):
        self.screen.addstr(y, x, phrase, curses.color_pair(color))

    def key_pressed(self):
        key = self.screen.getch()
        return key

    def refresh(self):
        self.screen.refresh()

    def destroy(self):
        self.screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
