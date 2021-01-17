import curses

class Window(object):
    """
    Class that implements a base window to be displayed in a Screen object
    """

    def __init__(self, x, y, xw, yw):
        """
        Constructor
        :param x horizontal position on the screen
        :param y vertical position on the screen
        :param xw horizontal width of the window
        :param yw vertical width of the window
        :param cp color pair to use, defaults to white on black
        """
        self._x = x
        self._y = y
        self._xw = xw
        self._yw = yw
        self._cp = cp
        self._window = curses.newwin(yw, xw, y, x)

    def print(self, phrase):
        self._window.addstr(phrase)

    def print_at(self, x, y, phrase):
        self._window.addstr(y, x, phrase)

    def print_with_color(self, phrase, cp=None):
        if cp:
            self._window.addstr(phrase, curses.color_pair(cp))
        else:
            self._window.addstr(phrase, curses.color_pair(self._cp))

    def print_at_with_color(self, x, y, phrase, cp=None):
        if cp:
            self._window.addstr(y, x, phrase, curses.color_pair(cp))
        else:
            self._window.addstr(y, x, phrase, curses.color_pair(self._cp))

    def erase(self):
        self._window.erase()

    def refresh(self):
        self._window.refresh()
