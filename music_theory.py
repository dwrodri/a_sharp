from enum import Enum

class Note(Enum):
    A = (0, 'A')
    A_sharp = (1, 'A#')
    B_flat = (1, 'Bb')
    B = (2, 'B')
    C_flat = (2, 'Cb')
    B_sharp = (3, 'B#')
    C = (3, 'C')
    C_sharp = (4, 'C#')
    D_flat = (4, 'Db')
    D = (5, 'D')
    D_sharp = (6, 'D#')
    E_flat = (6, 'Eb')
    E = (7, 'E')
    F_flat = (7, 'Fb')
    E_sharp = (8, 'E#')
    F = (8, 'F')
    F_sharp = (9, 'F#')
    G_flat = (9, 'Gb')
    G = (10, 'G')
    G_sharp = (11, 'G#')
    A_flat = (11, 'Ab')
    def __init__(self, value, symbol):
       self.number = value
       self.symbol = symbol

class Scale(Enum):
    Major=[0,2,4,5,7,9,11]
    Minor=[0,2,3,5,7,8,10]
    Harmonic_Minor=[0,2,3,5,7,8,11]
    Melodic_Minor=[0,2,3,5,7,9,11]
    Major_Pentatonic=[0,2,4,7,9]
    Minor_Pentatonic=[0,3,5,7,10]
    Diminished=[0,2,3,5,6,8,9,11]
    Wholetone=[0,2,4,6,8,10]
    Ionian=[0,2,4,5,7,9,11]
    Dorian=[0,2,3,5,79,10]
    Phrygian=[0,1,3,5,7,8,10]
    Lydian=[0,2,4,6,7,9,11]
    Mixolydian=[0,2,4,5,7,9,10]
    Aeolian=[0,2,3,5,7,8,10]
    Locrian=[0,1,3,5,6,8,10]
    Chromatic=[0,1,2,3,4,5,6,7,8,9,10,11]
    def __init__(self, displacement_map):
        self.displacement_map = displacement_map

class Intervals(Enum):
    min2 = (1, 'm2')
    maj2 = (2, 'M2')
    min3 = (3, 'm3')
    maj3 = (4, 'M3')
    per4 = (5, 'P4')
    aug4 = (6, 'A4')
    per5 = (7, 'P5')
    min6 = (8, 'm6')
    maj6 = (9, 'M6')
    min7 = (10, 'm7')
    maj7 = (11, 'M7')


class chordFlavors(Enum):
    maj=[0,4,7]
    minor=[0,3,7]
    dim=[0,3,6]
    # maj_7=[0,4,7,11]
    # min_7=[0,3,7,10]
    # dom_7=[0,4,7,10]
    # dim_full=[0,3,6,9]
    # dim_half=[0,3,6,10]

class chordQuality(Enum):
    I = ("I", [0,])
    ii = ("ii", [0,])
    iii = ("iii", [0,])
    IV = ("IV", [0,])
    V = ("V", [0,])
    vi = ("vi", [0,])
    vii = ("vii", [0,])
