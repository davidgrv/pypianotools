import math


def freq_to_note(freq):
    key_num = round(12 * (math.log2(freq / 440)) + 49)
    note_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    oct_num = (key_num - 1) // 12
    note_index = (key_num - 1) % 12
    note = f'{note_names[note_index]}{oct_num}'

    return note


def note_to_freq(note, decimal_places=3):
    a4_freq = 440.0
    key_mapping = {
        "C": -9, "C#": -8,
        "D": -7, "D#": -6,
        "E": -5,
        "F": -4, "F#": -3,
        "G": -2, "G#": -1,
        "A": 0, "A#": 1,
        "B": 2
    }

    note_name = note[:-1]
    oct_num = int(note[-1])
    semitone_offset = key_mapping[note_name] + (oct_num - 4) * 12
    freq = a4_freq * (2 ** (semitone_offset / 12))
    freq = round(freq, decimal_places)

    return freq


def note_to_midi(note):
    note_mapping = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}

    if len(note) < 2 or not note[0].isalpha():
        raise ValueError("Invalid input: enter a valid note (e.g. A4)")

    note_name = note[:-1]
    octave = int(note[-1])

    midi_note = note_mapping[note_name.upper()] + (octave + 1) * 12

    return midi_note


def note_to_key_number(note):
    note_mapping = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10,
                    'B': 11}

    if len(note) < 2 or not note[0].isalpha():
        raise ValueError("Invalid input: enter a valid piano key (e.g. A4)")

    note_name = note[:-1]
    octave = int(note[-1])

    piano_key_num = (note_mapping[note_name.upper()] + (octave + 1) * 12) - 20

    return piano_key_num
