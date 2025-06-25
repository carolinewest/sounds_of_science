import pandas as pd

class AAToMidiCSV:
    '''
    Converts an amino acid sequence to a MIDI CSV format.
    The amino acids are mapped to MIDI note numbers, and the output is saved as a CSV file.
    The default mapping is as follows:
    A=60, C=62, D=64, E=65, F=67, G=69, H=71,
    I=60, K=62, L=64, M=65, N=67, P=69, Q=71,
    R=60, S=62, T=64, V=65, W=67, Y=69, *=0
    The default values for the MIDI parameters are:
    Velocity=63, Instrument=1, Channel=0, Track=0,
    Tempo=120, Pan=64, Volume=100, Expression=80, Duration=1.0
    The output CSV file will have the following columns:
    Time, Note, Duration, Velocity, Instrument, Channel, Track, Tempo, Pan, Volume, Expression
    The Time column is the cumulative time for each note, starting from 0.0.
    '''
    def __init__(self, aa_sequence, csv_out="output.csv"):
        self.aa_sequence = aa_sequence.upper()
        self.csv_out = csv_out
        self.aa_to_midi = {
            'A': 60, 'C': 62, 'D': 64, 'E': 65, 'F': 67, 'G': 69, 'H': 71,
            'I': 60, 'K': 62, 'L': 64, 'M': 65, 'N': 67, 'P': 69, 'Q': 71,
            'R': 60, 'S': 62, 'T': 64, 'V': 65, 'W': 67, 'Y': 69, '*': 0
        }
        self.defaults = {
            "Velocity": 63, "Instrument": 1, "Channel": 0, "Track": 0,
            "Tempo": 120, "Pan": 64, "Volume": 100, "Expression": 80,
            "Duration": 1.0
        }

    def convert_to_midi_rows(self):
        '''
        Converts the amino acid sequence to MIDI rows.
        Each row corresponds to a note in the MIDI format.
        The Time column is the cumulative time for each note, starting from 0.0.
        Sets the default values for the MIDI parameters.
        The output is a list of dictionaries, each representing a row in the CSV.
        '''
        time = 0.0
        data = []
        #for every amino acid in the sequence, get the corresponding MIDI note
        # and create a row with the default values
        for aa in self.aa_sequence:
            note = self.aa_to_midi.get(aa, 60)  # Default to C4 for unknowns
            row = {
                "Time": time,
                "Note": note,
                "Duration": self.defaults["Duration"],
                "Velocity": self.defaults["Velocity"],
                "Instrument": self.defaults["Instrument"],
                "Channel": self.defaults["Channel"],
                "Track": self.defaults["Track"],
                "Tempo": self.defaults["Tempo"],
                "Pan": self.defaults["Pan"],
                "Volume": self.defaults["Volume"],
                "Expression": self.defaults["Expression"]
            }
            data.append(row)
            time += self.defaults["Duration"]
        return data

    def process(self, save=True):
        '''
        Processes the amino acid sequence and converts it to MIDI CSV format.
        '''
        # Convert the amino acid sequence to MIDI rows
        if not self.aa_sequence:
            raise ValueError("Amino acid sequence is empty. Please provide a valid sequence.")      
        rows = self.convert_to_midi_rows()
        df = pd.DataFrame(rows)
        
        # Reorder columns to match MIDI CSV format
        if save:
            df.to_csv(self.csv_out, index=False)
            print(f"CSV exported to {self.csv_out}")
        return df
