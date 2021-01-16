from .notes import Note, Notes

class Chords:
    """
    Class that holds chords definition
    """

    _CHORDS = {
        'maj': (0, 4, 7),
        'min': (0, 3, 7),
        '5': (0, 7),
        '6': (0, 4, 7, 9),
        '7': (0, 4, 7, 10),
        '9': (0, 4, 7, 10, 14),
        '11': (0, 4, 7, 10, 14, 17),
        '13': (0, 4, 7, 10, 14, 21),
        'dim': (0, 3, 6),
        'dim7': (0, 3, 6, 9),
        'aug': (0, 4, 8),
        'sus2': (0, 2, 7),
        'sus4': (0, 5, 7),
        'sus2sus4': (0, 2, 5, 7),
        'maj7': (0, 4, 7, 11),
        'min7': (0, 3, 7, 10),
        '7sus4': (0, 5, 7, 10),
        'maj9': (0, 4, 7, 11, 14),
        'maj11': (0, 4, 7, 11, 14, 17),
        'maj13': (0, 4, 7, 11, 14, 21),
        'add9': (0, 4, 7, 14),
        '6add9': (0, 4, 7, 9, 14),
        'maj7b5': (0, 4, 6, 11),
        'maj7#5': (0, 4, 8, 11),
        'min6': (0, 3, 7, 9),
        'min9': (0, 3, 7, 10, 14),
        'min11': (0, 3, 7, 10, 14, 11),
        'min13': (0, 3, 7, 10, 14, 11, 21),
        '7b5': (0, 4, 6, 10),
        '7#5': (0, 4, 8, 10),
        '7b9': (0, 4, 7, 10, 13),
        '7#9': (0, 4, 7, 10, 15),
        '9b5': (0, 4, 6, 10, 14),
        '9#5': (0, 4, 8, 10, 14),
    }

    @classmethod
    def get_chord(cls, name):
        try:
            return cls._CHORDS[name]
        except KeyError:
            return cls._CHORDS['maj']


class Chord:

    def __init__(self, name='maj', base=60):

        # Store class properties
        self._name = name
        self._base = base

        # Compute chord from chosen name and base
        self.set_chord(name, base)

    def set_chord(self, name, base):

        # Initialize extended scale
        self._chord = []

        # Get base chord degrees from chords definition
        base_chord = Chords.get_chord(name)

        # Compute chord starting from passed base note
        i = 0
        while (i < len(base_chord) and
               Notes.get_name(base + base_chord[i])):
            self._chord.append(Note(base + base_chord[i]))
            i += 1
        self._size = len(self._chord)

    def get_size(self):
        return self._size

    def get_note(self, index):
        return self._chord[index]
