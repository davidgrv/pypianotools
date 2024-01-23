import math

note_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
note_mapping = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}


def freq_to_note(freq):
    """
    Converts frequency in Hertz to the nearest note using scientific pitch notation.
    Example: 441 Hz is nearest to A4 (440 Hz).
    :param freq: frequency in Hertz as a float or int
    :return: note string expressed in scientific pitch notation (e.g. A4)
    """
    key_num = round(12 * (math.log2(freq / 440)) + 49)
    oct_num = (key_num - 1) // 12
    note_index = (key_num - 1) % 12
    note = f'{note_names[note_index]}{oct_num}'

    return note


def note_to_freq(note, decimal_places=3):
    """
    Converts a note expressed in scientific pitch notation (e.g. A4)
    to its respective frequency in Hertz (440 Hz).
    :param note: Note string expressed in scientific pitch notation (e.g. A4)
    :param decimal_places: rounds returned float to passed number of decimal places
    :return: frequency float in Hz
    """
    a4_freq = 440.000
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
    """
    Converts a note expressed in scientific pitch notation (e.g. A4)
    to its respective MIDI note Number (69).
    :param note: note string expressed in scientific pitch notation (e.g. A4)
    :return: MIDI note number as an int
    """
    if len(note) < 2 or not note[0].isalpha():
        raise ValueError("Invalid input: enter a valid note (e.g. A4)")

    note_name = note[:-1]
    oct = int(note[-1])

    midi_note = note_mapping[note_name.upper()] + (oct + 1) * 12

    return midi_note


def note_to_key_number(note):
    """
    Takes a note expressed in scientific pitch notation and returns its key number
    on the piano. Assumes the piano has 88 keys total starting from A0 up to C8.
    :param note: note string expressed in scientific pitch notation (e.g. A4)
    :return: piano key number as an int
    """
    if len(note) < 2 or not note[0].isalpha():
        raise ValueError("Invalid input: enter a valid note (e.g. A4)")

    note_name = note[:-1]
    oct = int(note[-1])

    piano_key_num = (note_mapping[note_name.upper()] + (oct + 1) * 12) - 20

    if (piano_key_num < 0) or (piano_key_num > 88):
        raise ValueError("Invalid input: note must be between A0 and C8 (inclusive) "
                         "on an 88 key piano")

    return piano_key_num
