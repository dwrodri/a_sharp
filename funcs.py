#! /usr/local/bin/python3
from music_theory import Note, Scale, chordQuality, chordFlavors
import pprint

ACTIVE_ROOT = Note.C
ACTIVE_SCALE = Scale.Major
USE_FLATS = False
MASTER_TUNING = [Note.E, Note.B, Note.G, Note.D, Note.A, Note.E]
FRETS_PER_STRING= 24
AMT_OF_STRINGS= 6
FRET_MATRIX = [[],[],[],[],[],[]]

def  fretMatrixIsEmpty(): #works!
    return not any(FRET_MATRIX)

def populateFretboard():
    for i in range(len(MASTER_TUNING)):
        FRET_MATRIX[i].append(MASTER_TUNING[i].number)
    for string in FRET_MATRIX:
        string_scale = Scale.Chromatic.displacement_map[Scale.Chromatic.displacement_map.index(string[0]):]+Scale.Chromatic.displacement_map[:Scale.Chromatic.displacement_map.index(string[0])]
        for j in range(1,FRETS_PER_STRING+1):
            string.append((string_scale[j%12:]+string_scale[:j%12])[0])

def wasteOfMyTime(root_note, scale):
    note_array = getScaleNotesEnums(root_note, scale)

    for i in range(len(MASTER_TUNING)):
        FRET_MATRIX[i].append(MASTER_TUNING)
    for string in FRET_MATRIX:
        string_scale = note_array[note_array.index(string[0]):]+note_array[:note_array.index(string[0])]
        for j in range(1,FRETS_PER_STRING):
            string.append(note_array.rotate(j%len(string_scale)))


def getFretsForChord(chord_notes):
    """
    """
    pass

def getChordID(chord_notes):
    pass

def getChordNotesNumbers(root_note, chord_flavor):
    noteVals = []
    for displacement in chord_flavor.value:
        noteVals.append((root_note.number + displacement)%12)
    return noteVals


def getChordNotesNames(root_note, chord_flavor):
    noteNums = getChordNotesNumbers(root_note, chord_flavor)
    noteSymbols = []
    noteSymbols.append(root_note.symbol)
    for i in range(1, len(noteNums)):
        candidateSymbols = [x.symbol for x in Note if x.number is noteNums[i]]
        candidateSymbols = list(filter(lambda n: noteSymbols[i-1] not in n, candidateSymbols)) # remove potential repeats
        if USE_FLATS: # check global toggle
            candidateSymbols = list(filter(lambda n: "#" not in n, candidateSymbols))  # filter out sharps
        noteSymbols.append(candidateSymbols[0])
    return noteSymbols

def getFretsWithNote(note):
    desiredFretPositions = []
    for i in range(len(FRET_MATRIX)):
        for j in range(len(FRET_MATRIX[i])):
            if FRET_MATRIX[i][j] is note:
                desiredFretPositions.append([i,j])
    return desiredFretPositions

def getEquivalentFrets(string_pos, fret_pos):
    """
    Gets the values of our enum implementation

    :param note: note name wanted
    :return: array of all enum note names on the fretboard that match the input
    """
    key = FRET_MATRIX[string_pos, fret_pos]
    desiredPositions = []
    for i in range(len(FRET_MATRIX)):
        for j in range(len(FRET_MATRIX[i])):
            if (string_pos is not i) and (fret_pos is not j) and (key is FRET_MATRIX[i][j]):
                desiredPositions.append([i,j])
    return desiredPositions


def getScalesWithChord(note_array):  # works!
    """
    Where derek goes crazy trying to implement a Scale map reduction

    :param note_array: array of note Enums to use as filter
    :return: list of scales that can be used with the chord
    """
    desiredScales = {}
    candidateScales = {}
    chordNames = [x.symbol for x in note_array]
    for s in Scale:
        candidateScales.setdefault(note_array[0].symbol + ' ' + s.name, getScaleNotesNames(note_array[0], s))

    for key in candidateScales:
        a = [elem for elem in chordNames if elem in candidateScales[key]]
        b = [elem for elem in candidateScales[key] if elem in chordNames]
        if a == b and a == chordNames:
            desiredScales.setdefault(key, candidateScales[key])
    return desiredScales

def getScaleNotesEnums(root_note, scale):
    names = getScaleNotesNames(root_note, scale)
    return [x for x in Note if x.symbol in names]

def getScaleNotesNames(root_note, scale): # works!
    """
    Used to build a full scale from a root note and a scale name

    :param root_note: starting note of the scale
    :param scale: the scale name
    :return: array of note names
    """
    noteNums = getScaleNotesNumbers(root_note, scale)
    noteSymbols = []
    noteSymbols.append(root_note.symbol)
    for i in range(1, len(noteNums)):
        candidateSymbols = [x.symbol for x in Note if x.number is noteNums[i]]
        candidateSymbols = list(filter(lambda n: noteSymbols[i-1] not in n, candidateSymbols)) # remove potential repeats
        if USE_FLATS: # check global toggle
            candidateSymbols = list(filter(lambda n: "#" not in n, candidateSymbols))  # filter out sharps
        noteSymbols.append(candidateSymbols[0])
    return noteSymbols


def getScaleNotesNumbers(root_note, scale): # works!
    """
    Gets the values of our enum implementation

    :param root_note: starting note of the scale
    :param scale: the scale name
    :return: array of enum note numbers
    """
    noteVals = []
    for displacement in scale.displacement_map:
        noteVals.append((root_note.number + displacement)%12)
    return noteVals

def findNote(sym):
    return [x for x in Note if x.symbol == sym][0]

def findScale(sym):
    return [x for x in Scale if x.name == sym][0]

def resolveNote(value):
    candidates = [x.symbol for x in Note if x.number is value]
    if any(map(lambda n: len(n) is 1, candidates)):
        return sorted(candidates, key=len)[0]
    elif USE_FLATS:
        return list(filter(lambda x: 'b' in x, candidates))[0]
    else:
        return list(filter(lambda x: '#' in x, candidates))[0]

def searchScales(query_string): # works!
    """
    Tries to find a the scale from our scales enum

    :param query_string: the scale name
    :return: the found scale
    """
    names = [x.name for x in Scale]
    return [x for x in names if query_string in x][0]

def generateASCIIFretboard(name):
    return 'fretboard'

def findChord(sym):
    return [x for x in chordFlavors if x.name == sym][0]

def renderChordCSV():
    note_names = []
    csvContents = {}
    for displacement in Scale.Chromatic.displacement_map:
        note_names.append(resolveNote(displacement))

    for note in note_names:
        rotated = note_names[note_names.index(note):] + note_names[:note_names.index(note)]
        for flavor in chordFlavors:
            desiredNoteNames = []
            for i in range(3):
                desiredNoteNames.append(rotated[flavor.value[i]])
            chordName = note + ' ' + flavor.name
            csvContents[chordName] = desiredNoteNames

    return csvContents

if __name__ == '__main__':
    part1 = renderChordCSV()
    USE_FLATS = True
    part2 = renderChordCSV()
    part1.update(part2)
    pprint.pprint(part1)
