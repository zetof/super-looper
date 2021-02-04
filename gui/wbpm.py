from .window import Window
from .palette import Palette


class WBpm(Window):

    def __init__(self, bpm=120, active=True):
        super(WBpm, self).__init__(1, 1, 40, 1, active)
        self._bpm = bpm

    def update(self):
        self.erase()
        self.print('BPM: ', Palette.NORMAL)
        self.print(str(self._bpm), Palette.HIGHLIGHTED)

    def bpm_update(self, data):
        self._bpm = data[2]
        self.update()
