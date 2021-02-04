from .window import Window
from .palette import Palette

class WMetronome(Window):

    def __init__(self, bar=0, beat=0, active=True):
        super(WMetronome, self).__init__(1, 2, 40, 1, active)
        self._bar = bar
        self._beat = beat

    def update(self):
        if self.is_active():
            self.erase()
            self.print('BAR: ', Palette.NORMAL)
            self.print(str(self._bar), Palette.HIGHLIGHTED)
            self.print(' BEAT: ', Palette.NORMAL)
            self.print(str(self._beat), Palette.HIGHLIGHTED)

    def tick_update(self, beat, bar, **kwarg):
        self._beat = beat
        self._bar = bar
        self.update()