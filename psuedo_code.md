This project transforms DNA sequences into music. Each part of the genetic code influences different parts of a musical note — like pitch, speed, rhythm, and even the instrument. It helps us "hear" the biology.

1. Get the Genetic Sequences

    Open a .fasta file with DNA sequences.

    Save both the DNA and the protein (amino acid) version of each sequence.

2. Prepare Information for Notes

    For each amino acid:

        Decide the musical pitch (like a note on the piano).

        Choose how long the note lasts based on the size of the amino acid.

        Set the playing speed (tempo) based on repeated parts in the DNA.

        Use GC content (how much G and C there is) to decide how hard the note is played (velocity).

        Detect special patterns (motifs) and change the instrument when they show up.

        If there's a stop signal (*), play a pause (rest).

3. Build the Music Table

    For each amino acid in a sequence:

        Add a new row to the table with all its musical info:

            Which protein it's from.

            What note it plays (pitch).

            How long it lasts (duration).

            How fast it plays (tempo).

            How hard it's hit (velocity).

            What instrument it uses.

            Whether it’s a real note or a rest.

4. Make the Music

    Use the table to generate a MIDI file (a digital sheet of music).

    Save it so it can be played back with music software.

Extra Notes

    If any part of a DNA sequence doesn’t fit perfectly into groups of 3 (to make amino acids), add placeholder letters to make it work.

    Unknown or untranslatable amino acids get a default sound or become rests.


Class BioToMusicPipeline:
    # ---- Initialization ----
    Function __init__(self, file_path: String, is_protein: Bool):
        self.file_path = file_path
        self.is_protein = is_protein
        self.sequences = {}         # {header: sequence}
        self.translated = {}        # {header: protein sequence}
        self.gc_content = {}        # {header: gc content as float}
        self.orfs = {}              # {header: list of (start, stop)}
        self.repeats = {}           # {aa: [(position, count)]}
        self.notes = {}             # {header: musical note sequence}
        self.instrument_map = {}    # {motif: instrument name}

    # ---- Load sequences ----
    Function load_fasta():
        If is_protein:
            Parse file as protein FASTA
        Else:
            Parse file as nucleotide FASTA

        Store {header: sequence} in self.sequences

    # ---- Translate to protein ----
    Function translate_sequences(reading_frame = 0):
        For each nucleotide sequence:
            shift by reading_frame
            translate to protein (stop or not)
            store in self.translated

    # ---- Create motifs and map to instruments ----
    Function detect_motifs_and_map_instruments(motif_length: Integer):
        For each protein sequence:
            slide window of length motif_length
            for each motif:
                assign to a predefined instrument
                store in self.instrument_map

    # ---- ORF finder ----
    Function find_orfs():
        For each nucleotide sequence:
            Scan for ATG (start codon)
            Find nearest in-frame stop codon (TAA, TAG, TGA)
            Store (start, stop) coordinates in self.orfs

    # ---- GC content calculator ----
    Function calculate_gc_content():
        For each nucleotide sequence:
            count G and C
            divide by sequence length
            store as float in self.gc_content

    # ---- Find amino acid repeats ----
    Function find_repeats(min_repeat_length: Integer):
        For each amino acid sequence:
            For each character:
                Track repeated amino acid runs
                If repeat length >= min_repeat_length:
                    store (position, repeat length) in self.repeats

    # ---- Convert to musical notes ----
    Function aa_to_notes(note_dict: Dict):
        For each amino acid sequence:
            convert each amino acid to corresponding note
            store in self.notes

    # ---- Render score ----
    Function write_score(output_file: String):
        For each note sequence:
            Write to output file in pseudo-musical score format
            Include instrument mapping if available

    # ---- Run all ----
    Function run_pipeline():
        load_fasta()
        If not is_protein:
            translate_sequences()
            find_orfs()
            calculate_gc_content()
        find_repeats(min_repeat_length=3)
        detect_motifs_and_map_instruments(motif_length=3)
        aa_to_notes(note_dict=your_aa_to_note_dict)
        write_score(output_file="musical_score.txt")