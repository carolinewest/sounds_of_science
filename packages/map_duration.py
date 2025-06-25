"""
Dictionaries to connect different note values to amino acids and their weights.
The note values are based on MIDI note numbers, and the amino acid size are used to determine the duration of each note.
"""
note_to_aa = {
    60: 'X',  # Default or unknown
    61: 'R', 62: 'N', 63: 'D', 64: 'C', 65: 'E', 66: 'Q', 67: 'G',
    68: 'H', 69: 'I', 70: 'L', 71: 'K', 72: 'M', 73: 'F', 74: 'P',
    75: 'S', 76: 'T', 77: 'W', 78: 'Y', 79: 'V', 80: 'A'
}

aa_weights = {
    'A': 'sixteenth', 'G': 'sixteenth', 'S': 'sixteenth',
    'N': 'eighth', 'D': 'eighth', 'C': 'eighth', 'P': 'eighth', 'T': 'eighth',
    'Q': 'quarter', 'E': 'quarter', 'H': 'quarter', 'V': 'quarter',
    'R': 'half', 'I': 'half', 'L': 'half', 'K': 'half', 'M': 'half',
    'F': 'whole', 'W': 'whole', 'Y': 'whole'
}

durations = {
    'sixteenth': 0.25,
    'eighth': 0.5,
    'quarter': 1.0,
    'half': 2,
    'whole': 4
}

# Duration mapping function
def map_note_to_duration(note):
    aa = note_to_aa.get(note, 'X')
    if aa == 'X' or aa == '*':
        return 1.0  # Default rest duration: quarter note
    size = aa_weights.get(aa.upper(), 'quarter')
    return durations[size]

# Pitch mapping function (0 = rest)
def map_note_to_pitch(note):
    aa = note_to_aa.get(note, 'X')
    return 0 if aa == 'X' or aa == '*' else note