import curses

class W_Metronome:

    def __init__(self):
        self._tick = '0'
        self._beat = '0'
        self._bar = '0'
        self._window = curses.newwin(1, 40, 2, 1)
        curses.init_pair(3, 67, curses.COLOR_BLACK)
        curses.init_pair(4, 255, curses.COLOR_BLACK)

    def update(self):
        self._window.erase()
        self._window.addstr('BAR: ', curses.color_pair(3))
        self._window.addstr(self._bar, curses.color_pair(4))
        self._window.addstr(' BEAT: ', curses.color_pair(3))
        self._window.addstr(self._beat, curses.color_pair(4))
        self._window.addstr(' TICK: ', curses.color_pair(3))
        self._window.addstr(self._tick, curses.color_pair(4))

    def refresh(self):
        self._window.refresh()

    def tick_update(self, tick):
        self._tick = str(tick)
        self.update()

    def beat_update(self, beat):
        self._beat = str(beat)

    def bar_update(self, bar):
        self._bar = str(bar)
