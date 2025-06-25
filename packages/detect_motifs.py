# motif_detection.py
from Bio import SeqIO
import pandas as pd

# Motif to biological explanation and percussion mapping
motif_to_instrument = {
    "TATAAA": "violin",
    "TATAAT": "violin",
    "AATAAA": "choir",
    "CAAT": "flute",
    "CCAAT": "flute",
    "GCGCGC": "metallic synth",
    "CGCGCG": "metallic synth",
    "GGATCC": "goblins",
    "AAGCTT": "goblins",
    "GAATTC": "goblins",
    "ATATAT": "sci-fi",
    "TATATA": "sci-fi",
    "TTAGGG": "space bass",
    "GTAGAG": "voice oohs",
    "ATG": "electric bass",
    "TAG": "dark synth",
    "TGA": "dark synth",
    "TAA": "dark synth"
}

# MIDI percussion mapping
motif_to_drum = {
    "TATAAA": 56, "TATAAT": 56,       # Cowbell
    "AATAAA": 57,                     # Crash cymbal 2
    "CAAT": 51, "CCAAT": 51,          # Ride cymbal 1
    "GCGCGC": 39, "CGCGCG": 39,       # Hand clap
    "GGATCC": 40, "AAGCTT": 40, "GAATTC": 40,  # Electric snare
    "ATATAT": 38, "TATATA": 38,       # Acoustic snare
    "TTAGGG": 35,                     # Bass drum
    "GTAGAG": 48, "ATG": 50,          # Toms
    "TAG": 49, "TGA": 49, "TAA": 49   # Crash cymbals
}

def generate_motif_hits(fasta_file,length):
    """
    Given a FASTA file, find motifs and generate a list of hits, 
    including motif, instrument, percussion, and amino acid positions.
    Returns a DataFrame of the motif hits.
    """
    # Read sequence from FASTA file
    sequences = list(SeqIO.parse(fasta_file, "fasta"))
    if not sequences:
        raise ValueError("No sequences found in the FASTA file.")
    
    instrument_list = [1 for i in range(length)]
    channel_list = [0 for i in range(length)]


    dna_sequence = str(sequences[0].seq).upper()
    print(f"DNA sequence: {dna_sequence[:50]}...")  # Print first 50 bases for debugging

    # Find motifs in DNA sequence
    motif_results = []
    for motif, instrument in motif_to_instrument.items():
        pos = 0
        while True:
            index = dna_sequence.find(motif, pos)
            if index == -1:
                break
            # Check if the instrument and drum note are correct
            if motif in motif_to_instrument:
                print(f"Found motif: {motif} at position {index} with instrument: {instrument} and drum note: {motif_to_drum[motif]}")
            else:
                print(f"ERROR: Motif {motif} not found in motif_to_instrument mapping!")

            motif_results.append({
                "motif": motif,
                "instrument": instrument,  # Correct instrument
                "start": index,
                "end": index + len(motif) - 1,
                "aa_position": index // 3,  # Position in the protein sequence
                "drum_note": motif_to_drum[motif],  # Correct drum note
                "channel": motif  # Add motif to the 'channel'
            })
            pos = index + 1

    # Sort motifs by amino acid position
    motif_results.sort(key=lambda x: x["aa_position"])

    # Convert to DataFrame
    df = pd.DataFrame(motif_results)

    # Debugging: Print the first few rows of the resulting DataFrame to ensure the instrument is assigned correctly
    print(f"Motif hits DataFrame:\n{df.head()}")  # Show the DataFrame with hits

    df_position_locations = df['aa_position'].to_list()
    df_instrument = df['drum_note'].to_list()


    for i in range(len(df_position_locations)):
        instrument_list[df_position_locations[i]] = df_instrument[i]
        channel_list[df_position_locations[i]] = 9

    return instrument_list, channel_list
