import curses
import atexit
from time import sleep
from .window import Window

class Screen:

    _windows = {}

    def __init__(self):
        self._screen = curses.initscr()
        if not curses.has_colors():
            self._screen.addstr("Application should be run in a 256 colors capable terminal !!!")
            self._screen.refresh()
            sleep(5)
            self.destroy()
            exit(1)
        self.height, self.width = self._screen.getmaxyx()
        curses.noecho()
        curses.curs_set(0)
        curses.cbreak()
        curses.start_color()
        curses.use_default_colors()
        atexit.register(self.destroy)
        self._screen.keypad(True)
        self._screen.nodelay(True)
        self._screen.refresh()

    def key_pressed(self):
        key = self._screen.getch()
        return key

    def refresh(self):
        self._screen.refresh()

    def add_window(self, name, window):
        self._windows.update({ name: window })

    def destroy(self):
        self._screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
