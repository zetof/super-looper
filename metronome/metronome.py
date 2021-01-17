from threading import Thread
from time import sleep
from .subscriber import Subscriber

class MetronomeEvents():

    TICK = 1
    BEAT = 2
    BAR = 3


class Metronome(Thread):

    _dispatcher = {
        MetronomeEvents.TICK: {},
        MetronomeEvents.BEAT: {},
        MetronomeEvents.BAR: {}
    }

    def __init__(self, bpm=120, bpb=4, tpb=4):
        self._bpm = bpm
        self._bpb = bpb
        self._tpb = tpb

        self._running = True
        self._paused = True
        self._set_delay()
        self._tick = 0
        self._bar = 0
        self._beat = 0

        Thread.__init__(self)

    def _set_delay(self):
        self._delay = 60 / self._bpm / self._tpb

    def run(self):
        while self._running:
            if not self._paused:
                self.inc_tick()
            sleep(self._delay)

    def stop(self):
        self._running = False

    def pause(self, data):
        self._paused = not self._paused

    def is_running(self):
        return self._running

    def subscribe(self, event_type, name, callback_class, callback_method,
                  enabled=True, with_data=False):
        try:
            subscriber = Subscriber(callback_class, callback_method, enabled,
                                    with_data)
            self._dispatcher[event_type].update({ name: subscriber })
            return True
        except KeyError:
            return False

    def unsubscribe(self, event_type, name):
        try:
            del self._dispatcher[event_type][name]
            return True
        except KeyError:
            return False

    def notify(self, event_type, **kwargs):
        try:
            for name, subscriber in self._dispatcher[event_type].items():
                subscriber.notify(**kwargs)
            return True
        except KeyError:
            return False

    def enable(self, event_type, name):
        try:
            self._dispatcher[event_type][name].enable()
            return True
        except KeyError:
            return False

    def disable(self, event_type, name):
        try:
            self._dispatcher[event_type][name].disable()
            return True
        except KeyError:
            return False

    def get_bpm(self):
        return self._bpm

    def set_bpm(self, data):
        if type(data) is list:
            self._bpm = data[2]
        else:
            self._bpm = data
        self._set_delay()

    def inc_tick(self):
        self._tick += 1
        if self._tick % self._tpb == 0:
            self._beat = (self._beat + 1) % self._bpb
            self.notify(MetronomeEvents.BEAT, beat=self._beat)
            if self._beat == 0:
                self._bar += 1
                self.notify(MetronomeEvents.BAR, bar=self._bar)
        self.notify(MetronomeEvents.TICK, tick=self._tick)
