from .window import Window
from .palette import Palette

class WMetronome(Window):

    def __init__(self, tick=0, beat=0, bar=0, active=True):
        super(WMetronome, self).__init__(1, 2, 40, 1, active)
        self._tick = tick
        self._beat = beat
        self._bar = bar

    def update(self):
        if self.is_active():
            self.erase()
            self.print('BAR: ', Palette.NORMAL)
            self.print(str(self._bar), Palette.HIGHLIGHTED)
            self.print(' BEAT: ', Palette.NORMAL)
            self.print(str(self._beat), Palette.HIGHLIGHTED)
            self.print(' TICK: ', Palette.NORMAL)
            self.print(str(self._tick), Palette.HIGHLIGHTED)

    def tick_update(self, tick):
        self._tick = tick
        self.update()

    def beat_update(self, beat):
        self._beat = beat

    def bar_update(self, bar):
        self._bar = bar
