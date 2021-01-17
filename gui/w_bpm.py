import curses

class W_Bpm:

    def __init__(self):
        self._bpm = '120'
        self._window = curses.newwin(1, 40, 1, 1)
        curses.init_pair(1, 67, curses.COLOR_BLACK)
        curses.init_pair(2, 255, curses.COLOR_BLACK)

    def update(self):
        self._window.erase()
        self._window.addstr('BPM: ', curses.color_pair(1))
        self._window.addstr(self._bpm, curses.color_pair(2))

    def refresh(self):
        self._window.refresh()

    def bpm_update(self, data):
        self._bpm = str(data[2])
        self.update()
