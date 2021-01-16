class Notes:
    """
    Class that allows manipulation of notes. Notes are defined by their names
    and translated to their midi equivalent. Only used as dictionary and
    reverse lookup dictionary with class methods. Notes are really implemented
    by the Note class.
    """

    _NAME_TO_MIDI = {
        'C2' : 36, 'C3' : 48, 'C4' : 60, 'C5' : 72, 'C6' : 84, 'C7' : 96,
        'C#2': 37, 'C#3': 49, 'C#4': 61, 'C#5': 73, 'C#6': 85, 'C#7': 97,
        'D2' : 38, 'D3' : 50, 'D4' : 62, 'D5' : 74, 'D6' : 86, 'D7' : 98,
        'D#2': 39, 'D#3': 51, 'D#4': 63, 'D#5': 75, 'D#6': 87, 'D#7': 99,
        'E2' : 40, 'E3' : 52, 'E4' : 64, 'E5' : 76, 'E6' : 88, 'E7' : 100,
        'F2' : 41, 'F3' : 53, 'F4' : 65, 'F5' : 77, 'F6' : 89, 'F7' : 101,
        'F#2': 42, 'F#3': 54, 'F#4': 66, 'F#5': 78, 'F#6': 90, 'F#7': 102,
        'G2' : 43, 'G3' : 55, 'G4' : 67, 'G5' : 79, 'G6' : 91, 'G7' : 103,
        'G#2': 44, 'G#3': 56, 'G#4': 68, 'G#5': 80, 'G#6': 92, 'G#7': 104,
        'A2' : 45, 'A3' : 57, 'A4' : 69, 'A5' : 81, 'A6' : 93, 'A7' : 105,
        'A#2': 46, 'A#3': 58, 'A#4': 70, 'A#5': 82, 'A#6': 94, 'A#7': 106,
        'B2' : 47, 'B3' : 59, 'B4' : 71, 'B5' : 83, 'B6' : 95, 'B7' : 107
    }

    _MIDI_TO_NAME = { value: key for key, value in _NAME_TO_MIDI.items() }

    @classmethod
    def get_midi(cls, name):
        try:
            return cls._NAME_TO_MIDI[name]
        except KeyError:
            return None

    @classmethod
    def get_name(cls, midi):
        try:
            return cls._MIDI_TO_NAME[midi]
        except KeyError:
            return None


class Note:
    """
    Class that instanciates a note. A note is defined by its name at creation
    time defaulting to a mid range 440Hz A if nothing has been provided.
    """

    def __init__(self, midi=None):
        if midi == None:
            self._midi = 69
        else:
            self._midi = midi
        self._name = Notes.get_name(self._midi)
        if not self._name:
            self._midi = None

    def get_name(self):
        return self._name

    def get_midi(self):
        return self._midi

    def set_name(self, name):
        self._name = name
        self._midi = Notes.get_midi(name)
        if not self._midi:
            self._name = None
        return self._midi

    def set_midi(self, midi):
        self._midi = midi
        self._name = Notes.get_name(self._midi)
        if not self._name:
            self._midi = None
        return self._name

    def add_degrees(self, degrees):
        return self.set_midi(self._midi + degrees)
