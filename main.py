from lpd8.lpd8 import LPD8
from lpd8.programs import Programs
from lpd8.pads import Pad, Pads
from lpd8.knobs import Knobs
from gui.screen import Screen
from gui.wbpm import WBpm
from gui.wmetronome import WMetronome
from time import sleep
from osc import Osc_Interface
from metronome.metronome import Metronome, MetronomeEvents

DEFAULT_BPM = 120

# Setting up the interface
screen = Screen()
w_bpm = WBpm()
w_metronome = WMetronome()
screen.add_window(w_bpm)
screen.add_window(w_metronome)
w_bpm.update()
w_metronome.update()

lpd8 = LPD8()
osc = Osc_Interface()
metronome = Metronome()

lpd8.set_knob_limits(Programs.PGM_4, Knobs.KNOB_1, 30, 180, steps=160)
lpd8.set_knob_value(Programs.PGM_4, Knobs.KNOB_1, DEFAULT_BPM)
lpd8.set_not_sticky_knob(Programs.PGM_4, Knobs.KNOB_1)
lpd8.set_pad_mode(Programs.PGM_4, Pads.PAD_5, Pad.SWITCH_MODE + Pad.BLINK_MODE)
lpd8.set_pad_switch_state(Programs.PGM_4, Pads.PAD_5, Pad.ON)
lpd8.subscribe(metronome, metronome.set_bpm, Programs.PGM_4, LPD8.CTRL, Knobs.KNOB_1)
lpd8.subscribe(w_bpm, w_bpm.bpm_update, Programs.PGM_4, LPD8.CTRL, Knobs.KNOB_1)
lpd8.subscribe(metronome, metronome.pause, Programs.PGM_4, LPD8.NOTE_ON, Pads.PAD_5)
metronome.subscribe(MetronomeEvents.BEAT, lpd8, lpd8.pad_update)
metronome.subscribe(MetronomeEvents.TICK, w_metronome, w_metronome.tick_update, with_data=True)
lpd8.pad_update()
lpd8.start()
osc.start()
metronome.start()

# We loop as long as test class allows it
running = True
while running:
    screen.refresh()
    action = screen.key_pressed()
    if action == ord('q'):
        running = False
    elif action == ord('r'):
        metronome.set_position()
    sleep(.01)

# We tidy up things and kill all processes
metronome.stop()
osc.stop()
lpd8.stop()
