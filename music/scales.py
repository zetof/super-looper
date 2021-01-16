from .notes import Note, Notes

class Scales:
    """
    Class that holds scales definition
    """

    # Dictionary defining a bunch of well known scales - Stolen from
    # SuperCollider with following script:
    # (
    # s = Scale.names;
    # s.do({arg item;
    # [Scale.all[item].name, Scale.all[item].degrees].postln;
    # });
    # )
    _SCALES = {
        'AEOLIAN': (0, 2, 3, 5, 7, 8, 10),
        'AHIRBHAIRAV': (0, 1, 4, 5, 7, 9, 10),
        'AJAM': (0, 4, 8, 10, 14, 18, 22),
        'ATHAR KURD': (0, 2, 6, 12, 14, 16, 22),
        'AUGMENTED': (0, 3, 4, 7, 8, 11),
        'AUGMENTED 2': (0, 1, 4, 5, 8, 9),
        'BARTOK': (0, 2, 4, 5, 7, 8, 10),
        'BASTANIKAR': (0, 3, 7, 10, 13, 15, 21),
        'BAYATI': (0, 3, 6, 10, 14, 16, 20),
        'BHAIRAV': (0, 1, 4, 5, 7, 8, 11),
        'CHINESE': (0, 4, 6, 7, 11),
        'CHROMATIC': (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
        'DIMINISHED': (0, 1, 3, 4, 6, 7, 9, 10),
        'DIMINISHED 2': (0, 2, 3, 5, 6, 8, 9, 11),
        'DORIAN': (0, 2, 3, 5, 7, 9, 10),
        'EGYPTIAN': (0, 2, 5, 7, 10),
        'ENIGMATIC': (0, 1, 4, 6, 8, 10, 11),
        'FARAHFAZA': (0, 4, 6, 10, 14, 16, 20),
        'GONG': (0, 2, 4, 7, 9),
        'HARMONIC MAJOR': (0, 2, 4, 5, 7, 8, 11),
        'HARMONIC MINOR': (0, 2, 3, 5, 7, 8, 11),
        'HEX AEOLIAN': (0, 3, 5, 7, 8, 10),
        'HEX DORIAN': (0, 2, 3, 5, 7, 10),
        'HEX MAJOR 6': (0, 2, 4, 5, 7, 9),
        'HEX MAJOR 7': (0, 2, 4, 7, 9, 11),
        'HEX PHRYGIAN': (0, 1, 3, 5, 8, 10),
        'HEX SUS': (0, 2, 5, 7, 9, 10),
        'HIJAZ': (0, 2, 8, 10, 14, 17, 20),
        'HIJAZ DESCENDING': (0, 2, 8, 10, 14, 16, 20),
        'HIJAZKAR': (0, 2, 8, 10, 14, 16, 22),
        'HINDU': (0, 2, 4, 5, 7, 8, 10),
        'HIRAJOSHI': (0, 2, 3, 7, 8),
        'HUNGARIAN MINOR': (0, 2, 3, 6, 7, 8, 11),
        'HUSSEINI': (0, 3, 6, 10, 14, 17, 21),
        'HUZAM': (0, 3, 7, 9, 15, 17, 21),
        'INDIAN': (0, 4, 5, 7, 10),
        'IONIAN': (0, 2, 4, 5, 7, 9, 11),
        'IRAQ': (0, 3, 7, 10, 13, 17, 21),
        'IWATO': (0, 1, 5, 6, 10),
        'JIAO': (0, 3, 5, 8, 10),
        'JIHARKAH': (0, 4, 8, 10, 14, 18, 21),
        'KARJIGHAR': (0, 3, 6, 10, 12, 18, 20),
        'KIJAZ KAR KURD': (0, 2, 8, 10, 14, 16, 22),
        'KUMAI': (0, 2, 3, 7, 9),
        'KURD': (0, 2, 6, 10, 14, 16, 20),
        'LEADING WHOLE TONE': (0, 2, 4, 6, 8, 10, 11),
        'LOCRIAN': (0, 1, 3, 5, 6, 8, 10),
        'LOCRIAN MAJOR': (0, 2, 4, 5, 6, 8, 10),
        'LYDIAN': (0, 2, 4, 6, 7, 9, 11),
        'LYDIAN MINOR': (0, 2, 4, 6, 7, 8, 10),
        'MAHUR': (0, 4, 7, 10, 14, 18, 22),
        'MAJOR': (0, 2, 4, 5, 7, 9, 11),
        'MAJOR PENTATONIC': (0, 2, 4, 7, 9),
        'MARVA': (0, 1, 4, 6, 7, 9, 11),
        'MELODIC MAJOR': (0, 2, 4, 5, 7, 8, 10),
        'MELODIC MINOR': (0, 2, 3, 5, 7, 9, 11),
        'MELODIC MINOR DESCENDING': (0, 2, 3, 5, 7, 8, 10),
        'NATURAL MINOR': (0, 2, 3, 5, 7, 8, 10),
        'MINOR PENTATONIC': (0, 3, 5, 7, 10),
        'MIXOLYDIAN': (0, 2, 4, 5, 7, 9, 10),
        'MURASSAH': (0, 4, 6, 10, 12, 18, 20),
        'MUSTAR': (0, 5, 7, 11, 13, 17, 21),
        'NAHAWAND': (0, 4, 6, 10, 14, 16, 22),
        'NAHAWAND DESCENDING': (0, 4, 6, 10, 14, 16, 20),
        'NAIRUZ': (0, 4, 7, 10, 14, 17, 20),
        'NAWA ATHAR': (0, 4, 6, 12, 14, 16, 22),
        'NEAPOLITAN MAJOR': (0, 1, 3, 5, 7, 9, 11),
        'NEAPOLITAN MINOR': (0, 1, 3, 5, 7, 8, 11),
        'NIKRIZ': (0, 4, 6, 12, 14, 18, 20),
        'PARTCH OTONALITY 1': (0, 8, 14, 20, 25, 34),
        'PARTCH OTONALITY 2': (0, 7, 13, 18, 27, 35),
        'PARTCH OTONALITY 3': (0, 6, 12, 21, 29, 36),
        'PARTCH OTONALITY 4': (0, 5, 15, 23, 30, 37),
        'PARTCH OTONALITY 5': (0, 10, 18, 25, 31, 38),
        'PARTCH OTONALITY 6': (0, 9, 16, 22, 28, 33),
        'PARTCH UTONALITY 1': (0, 9, 18, 23, 29, 35),
        'PARTCH UTONALITY 2': (0, 8, 16, 25, 30, 36),
        'PARTCH UTONALITY 3': (0, 7, 14, 22, 31, 37),
        'PARTCH UTONALITY 4': (0, 6, 13, 20, 28, 38),
        'PARTCH UTONALITY 5': (0, 5, 12, 18, 25, 33),
        'PARTCH UTONALITY 6': (0, 10, 15, 21, 27, 34),
        'PELOG': (0, 1, 3, 7, 8),
        'PHRYGIAN': (0, 1, 3, 5, 7, 8, 10),
        'PROMETHEUs': (0, 2, 4, 6, 11),
        'PURVI': (0, 1, 4, 6, 7, 8, 11),
        'RAST': (0, 4, 7, 10, 14, 18, 21),
        'RAST DESCENDING': (0, 4, 7, 10, 14, 18, 20),
        'RITUSEN': (0, 2, 5, 7, 9),
        'ROMANIAN MINOR': (0, 2, 3, 6, 7, 9, 10),
        'SABA': (0, 3, 6, 8, 12, 16, 20),
        'SCRIABIN': (0, 1, 4, 7, 9),
        'SHANG': (0, 2, 5, 7, 10),
        'SHAWQ AFZA': (0, 4, 8, 10, 14, 16, 22),
        'SIKAH': (0, 3, 7, 11, 14, 17, 21),
        'SIKAH DESCENDING': (0, 3, 7, 11, 13, 17, 21),
        'SPANISH': (0, 1, 4, 5, 7, 8, 10),
        'SUPER LOCRIAN': (0, 1, 3, 4, 6, 8, 10),
        'SUZNAK': (0, 4, 7, 10, 14, 16, 22),
        'TODI': (0, 1, 3, 6, 7, 8, 11),
        'USHAQ MASHRI': (0, 4, 6, 10, 14, 17, 21),
        'WHOLE TONE': (0, 2, 4, 6, 8, 10),
        'YAKAH': (0, 4, 7, 10, 14, 18, 21),
        'YAKAH DESCENDING': (0, 4, 7, 10, 14, 18, 20),
        'YU': (0, 3, 5, 7, 10),
        'ZAMZAM': (0, 2, 6, 8, 14, 16, 20),
        'ZANJARAN': (0, 2, 8, 10, 14, 18, 20),
        'ZHI': (0, 2, 5, 7, 9),
    }

    @classmethod
    def get_scale(cls, name):
        try:
            return cls._SCALES[name]
        except KeyError:
            return cls._SCALES['MAJOR']


class Scale:
    """
    Class that construct an extended scale based on scales definition
    The extended scale starts at a base note, follows degrees progression of
    selected scale definition until size is reached. If size is greater than
    length of selected scale, it is repeated with its successive octaves as
    long as size has not been reached
    """

    def __init__(self, name='MAJOR', base=60, size=7):
        """
        Class constructor
        :param name: Name of base scale used to built the extended scale
        :param base: A note object used to starting the extended scale
        :param size: Scale size, may be greater than the scale itself
        """

        # Store class properties
        self._name = name
        self._base = base

        # Compute extended scale from chosen name, base and size
        self.set_scale(name, base, size)

    def set_scale(self, name, base, size):
        """
        Computes an extended scale from passed parameters
        :param name: Name of base scale used to built the extended scale
        :param base: A note object used to starting the extended scale
        :param size: Scale size, may be greater than the scale itself
        :return: A computed extended scale as an array of note objects
        """

        # Initialize extended scale
        self._scale = []

        # Get base scale degrees from scales definition
        base_scale = Scales.get_scale(name)

        # As base is a midi note and may be derived from a note object, it
        # could be None if note object was not valid so we add a check here
        if not base:
            self._size = 0
        else:

            # If size > scale length, the extended scale is continued with its
            # successive octaves as long as necessary and finally truncated to
            # fit size
            shift = 0
            i = 0
            while (len(self._scale) < size and
                   Notes.get_name(base + base_scale[i] + shift)):
                self._scale.append(Note(base + base_scale[i] + shift))
                i += 1
                if i == len(base_scale):
                    i = 0
                    shift += 12
            self._size = len(self._scale)

    def get_scale(self):
        return self._scale

    def get_size(self):
        return self._size

    def get_note(self, index):
        return self._scale[index]
