import curses

class Window(object):
    """
    Class that implements a base window to be displayed in a Screen object
    """

    def __init__(self, x, y, width, height, active):
        """
        Constructor
        :param x horizontal position on the screen
        :param y vertical position on the screen
        :param xw horizontal width of the window
        :param yw vertical width of the window
        :param active ells if the window has to be displayed / refreshed
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._active = active
        self._window = curses.newwin(height, width, y, x)

    def is_active(self):
       return self._active

    def set_active(self):
        self._active = True

    def reset_active(self):
        self._active = False

    def print(self, string, cp=None, x=None, y=None):
        if cp:
            self._window.attron(curses.color_pair(cp))
        if x and y:
            self._window.addstr(y, x, string)
        else:
            self._window.addstr(string)

    def erase(self):
        self._window.erase()

    def refresh(self):
        if self._active:
            self._window.refresh()
