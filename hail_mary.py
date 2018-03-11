import funcs
import sys

def generateCSVChords(chordArr):
    rows = chordArr.split(' ')
    chordCSVDataString = ''
    for entry in rows:
        if 'b' in entry or '#' in entry:
            funcs.USE_FLATS = 'b'  in entry
            root_note_symbol = entry[:2]
            chord_name = entry[2:]
            chordCSVDataString = chordCSVDataString + root_note_symbol + ' ' + chord_name + ' '
            for note in funcs.getChordNotesNames(funcs.findNote(root_note_symbol), funcs.findChord(chord_name)):
                if 'b' in note:
                    note = note.replace('b', '_flat')
                elif '#' in note:
                    note = note.replace('#', '_sharp')
                chordCSVDataString = chordCSVDataString + ' ' + note + ' '
        else:
            root_note_symbol = entry[:1]
            chord_name = entry[1:]
            chordCSVDataString = chordCSVDataString + root_note_symbol + ' ' + chord_name
            for note in funcs.getChordNotesNames(funcs.findNote(root_note_symbol), funcs.findChord(chord_name)):
                if 'b' in note:
                    note = note.replace('b', '_flat')
                elif '#' in note:
                    note = note.replace('#', '_sharp')
                chordCSVDataString = chordCSVDataString + ' ' + note + ' '
        chordCSVDataString = chordCSVDataString + '\n'
    return chordCSVDataString

def generateCSVScales(scaleArr):
    rows = scaleArr.split(' ')
    scaleCSVDataString = ''
    for entry in rows:
        if 'b' in entry or '#' in entry:
            funcs.USE_FLATS = 'b' in entry
            root_note_symbol = entry[:2]
            scale_name = entry[2:]
            scale_enum = funcs.findScale(scale_name)
            scaleCSVDataString = scaleCSVDataString + root_note_symbol + ' ' + scale_name + ' '
            for note in funcs.getScaleNotesNames(funcs.findNote(root_note_symbol), funcs.findScale(scale_name)):
                if 'b' in note:
                    note = note.replace('b', '_flat')
                elif '#' in note:
                    note = note.replace('#', '_sharp')
                scaleCSVDataString = scaleCSVDataString + ' ' + note+ ' '

        else:
            root_note_symbol = entry[:1]
            scale_name = entry[1:]
            scaleCSVDataString = scaleCSVDataString + root_note_symbol + ' ' + scale_name + ' '
            for note in funcs.getScaleNotesNames(funcs.findNote(root_note_symbol), funcs.findScales(scale_name)):
                if 'b' in note:
                    note = note.replace('b', '_flat')
                elif '#' in note:
                    note = note.replace('#', '_sharp')
                scaleCSVDataString = scaleCSVDataString + ' ' + note+ ' '
        scaleCSVDataString = scaleCSVDataString + '\n'
    return scaleCSVDataString


if __name__ == '__main__':
    inputSpecs = sys.stdin.read()
    chordArray, scaleArray, outputPath = inputSpecs.split('0000')[:-1]
    print(generateCSVChords(chordArray))
    print(generateCSVScales(scaleArray))
