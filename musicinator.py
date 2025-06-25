import argparse
import pandas as pd
import numpy as np
import os
from packages.fasta_midi_converter import AAToMidiCSV
from packages.map_pitch import map_pitch
from packages.detect_motifs import generate_motif_hits
from packages.calculate_gc import calculate_gc_content
from packages.farruhs_packages import farruhs_packages
from packages.translate_file import translate_file
from packages.map_duration import map_note_to_duration, map_note_to_pitch
from mido import Message, MidiFile, MidiTrack
from packages.musicplots import plot_music_data

'''
Welcome to the Musicinator! This program converts a protein FASTA file into a MIDI file.
It uses the following packages:
- fasta_midi_converter: Converts amino acid sequences to MIDI format.
- map_pitch: Maps the pitch of the notes based on the amino acid sequence.
- detect_motifs: Detects motifs in the amino acid sequence and generates MIDI hits.
- calculate_gc: Calculates the GC content of the sequence and maps it to MIDI velocity.
- farruhs_packages: Applies additional transformations to the MIDI data.
- translate_file: Translates the FASTA file into an amino acid sequence.
- map_duration: Maps the duration of the notes based on the amino acid sequence.
- mido: A library for working with MIDI files.
- argparse: A library for parsing command line arguments.
- pandas: A library for data manipulation and analysis.
- numpy: A library for numerical computations.
- os: A library for interacting with the operating system.

'''
def main():
    # Parse command line arguments
    # The input file is the FASTA file containing the protein sequence.
    parser = argparse.ArgumentParser(description="Convert a protein FASTA to music")
    parser.add_argument("input_file", help="Input FASTA file")
    args = parser.parse_args()
    input_file = args.input_file

    #uses the translate_file function to convert the FASTA file into an amino acid sequence.
    aa_string = translate_file(input_file)
    
    #uses the AAToMidiCSV class to convert the amino acid sequence into a MIDI CSV format.
    # The output is saved as a CSV file named "standardized_output_music.csv".
    converter = AAToMidiCSV(aa_string, "standardized_output_music.csv")
    df = converter.process()

    #uses calculate_gc_content to calculate the GC content of the sequence.
    # The GC content is then mapped to MIDI velocity using a scaling factor of 1.27.
    # The window size for GC content calculation is set to 12.
    gc_profile = calculate_gc_content(input_file, window_size=12)
    df['Velocity'] = np.floor(np.array(gc_profile[:len(df)]) * 1.27 * 100) / 100


    #uses farruhs_packages to calculate the number of repeats in the sequence.
    #the number of repeats is then mapped to MIDI tempo.
    #With each repeat, the tempo is multiplied by a 1.15.
    df = farruhs_packages(aa_string, df)

    #uses the generate_motif_hits function to detect motifs in the amino acid sequence.
    #The motifs are then mapped to MIDI instrument and channel.
    entire_length = len(df['Time'].to_list())
    instrument_list, channel_list = generate_motif_hits(input_file, entire_length)
    df['Instrument'] = instrument_list
    df['Channel'] = channel_list

    #uses the map_note_to_duration function to map the notes to their corresponding durations.
    #The duration is then calculated based on the previous note's duration.
    #The time is calculated as the cumulative sum of the durations.
    #The time is then used to create a time column in the dataframe.
    df["Duration"] = df["Note"].apply(map_note_to_duration)
    df['Time'] = 0.0
    for i in range(1, len(df)):
        df.at[i,'Time'] = df.at[i - 1,'Time'] + df.at[i - 1,'Duration']

    
    #uses the map_note_to_pitch function to map the notes to their corresponding pitches.
    #the pitch is then modified based on a present open reading frame (ORF).
    #The ORF is detected using the map_pitch function.
    #The ORF is then used to modify the pitch of the notes in the dataframe.
    orfs = map_pitch(aa_string)
    for start, end in orfs:
        mask = (df.index >= start) & (df.index <= end) & (df['Note'] != 0)
        df.loc[mask, 'Note'] -= 1

    
    #saves the final output as a CSV file named "final_output_music.csv".
    print("Created final_output_music.csv")
    df.to_csv("final_output_music.csv", index=False)
    plot_music_data(df, gc_profile)

    #uses the mido library to create a MIDI file from the dataframe.
    midi_out = MidiFile()
    track = MidiTrack()
    midi_out.tracks.append(track)
    
    # Set the tempo and program change (instrument)
    track.append(Message('program_change', program=0, time=0))

    ticks_per_beat = midi_out.ticks_per_beat
    tempo = 500000
    time_multiplier = ticks_per_beat/(4) #is adjusted to 4 beats per measure

    # Set the tempo in microseconds per beat
    prev_time = 0
    
    # Loop through the dataframe and create MIDI messages
    #for each note in the dataframe.
    # The parameters for each note are set based on the values in the dataframe.
    # The note is played for the specified duration and velocity.
    # The time is calculated based on the previous note's time and the duration of the current note.
    # The note is then turned off after the specified duration.
    for _, row in df.iterrows():
        note = int(row['Note'])
        velocity = int(row.get('Velocity', 64))
        start_time = float(row['Time'])
        duration = float(row['Duration'])

        #start_time is converted to ticks based on the time multiplier.
        # The duration is also converted to ticks.
        # The previous time is updated to the current start time.
        start_ticks = int((start_time - prev_time) * time_multiplier)
        duration_ticks = int(duration * time_multiplier)
        prev_time = start_time

        # Append the note on and note off messages to the track
        # The note on message is sent with the specified note, velocity, and start time.
        # The note off message is sent with the specified note and duration.
        track.append(Message('note_on', note=note, velocity=velocity, time=start_ticks))
        track.append(Message('note_off', note=note, velocity=0, time=duration_ticks))
    print("Created final_output_music.mid")
    # Save the MIDI file
    # The MIDI file is saved as "final_output_music.mid".
    midi_out.save("final_output_music.mid")
    

if __name__ == "__main__":
    main()
