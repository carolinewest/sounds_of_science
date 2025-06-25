
# Sounds of Science

## Description
Here, we take in a FASTA file that has sequences and make music music
```
Given a DNA sequence, the program:

    Translates it to an amino acid sequence.

    Calculates GC content to determine note velocity.

    Maps amino acids to MIDI pitches and durations.

    Detects motifs and repeats to affect instrument and tempo.

    Outputs a structured MIDI table with all the musical parameters.
```
## Installation
- Python 3.8+
- [Biopython](https://biopython.org/) ver. 1.85
- Pandas ver. 2.2.3 : [https://pandas.pydata.org/]
- A MIDI writer library such as [`mido`](https://mido.readthedocs.io/en/latest/) or [`pretty_midi`](https://github.com/craffel/pretty-midi) (for generating MIDI files)

## Usage
### Input 
The input to this project is a **FASTA** file containing nucleotide sequences.

Each sequence must follow the standard FASTA format:
```fasta
>sequence_id
ATGCGTACGTAGCTAGCTAGCTAGCTAA
```
### Command Line
```bash
python musicinator.py --input path/to/sequences.fasta
```
### Output
- final_output_music.csv – Table of musical instructions (time, pitch, velocity, etc.)
- final_output_music.mid – MIDI file representing the translated sequence

## Recommendations
- FASTA file should not be large. Preferrably, it should be a few genes at most. Entire genomes aren't recommended to be run yet.
- If you have a Mac based computer, your system should have a default application that can open these files.
- A free software for Microsoft users: Audacity

## Musical Mapping
| Musical Parameter | Derived From            | Mapping Logic                                 |
|-------------------|-------------------------|------------------------------------------------|
| Pitch             | Open Reading Frames     | Specific MIDI values assigned to each AA       |
| Duration          | AA molecular size       | Mapped to note lengths (16th to whole notes)   |
| Velocity          | GC content of codons    | Scaled to MIDI velocity range (0–127)          |
| Tempo             | Repeat patterns         | Adjusted tempo based on sequence repetition    |
| Instrument        | Detected motifs         | Changes instrument (e.g., piano, violin)       |
| Rests             | Stop codons / Unknowns  | Represented with pitch = 0 (rest notes)        |

## Structure
```
sounds_of_silence/
├── main.py                    # Main logic and MIDI table builder
├── packages.py                # contains modules used in main.py
    ├── fasta_to_aa.py         # Translates FASTA sequences to amino acids
    ├── calculate_gc.py        # Computes GC content for nucleotide chunks
    ├── map_pitch.py           # Maps ORFs to MIDI pitch
    ├── map_duration.py        # Maps amino acids to note durations by size
    ├── detect_repeats.py      # Detects repeat patterns for tempo
    ├── detect_motifs.py       # Flags motif presence for instrument switching
    ├── get_tempo.py           # Returns a list with multipliers to be used on default tempo
    ├── multiplier.py          # Multiplies indexies of two lists together into a list and returns the resulting list
    ├── translate_file.py      # Translates entire fasta file and returns a string
    ├── farruhs_packages.py    # Combines get_tempo.py, multiplier.py, and translate_file.py into one 
├── LICENSE                    # Project license for use
├── PSEUDOCODE.md              # Project logic outline in pseudocode
├── flowchart.png              # Visuaal depiction of the process
└── README.md                  # Project description and usage guide
```

## Roadmap
- [x] Basic FASTA to MIDI table conversion
- [x] GC content analysis for velocity mapping
- [x] Amino acid translation and pitch/duration mapping
- [x] Motif detection for instrument changes
- [x] Repeat detection for tempo adjustment
- [x] Support for rest notes (stop codons/unknowns)
- [x] MIDI file generation
- [ ] MIDI file playback
- [ ] Web-based interface or visualization
- [ ] Integration with external music composition tools

# Authors and acknowledgment
- Caroline West: chill112@charlotte.ed | 801082826 
- Stephanie Wiedman: swiedma1@charlotte.edu | 80028576 
- Farruhjon Turgunov: fturguno@charlotte.edu | 801390682 
- Rishi Misra: rmisra1@charlotte.edu | 801144101 
- Sabrina Pinard: spinard@charlotte.edu | 801141865
- Abhishek Kasula: akasula@charlotte.edu | 801448648 

Special thanks to:
- The [Biopython](https://biopython.org/) community for their tools.
- OpenAI's ChatGPT for development assistance and debugging support.

## License
This project is licensed under the **GNU General Public License v3.0**.  
See the `LICENSE` file for more details.

## Project status
In development
