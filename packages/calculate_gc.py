from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def calculate_gc_content(fasta_path, window_size=12):
    """
    Calculates GC content for every 'window_size' nucleotides in a FASTA sequence.

    Args:
        fasta_path (str): Path to the FASTA file.
        window_size (int): Size of the sliding window (default is 12).

    Returns:
        List of tuples: Each tuple contains (start_position, gc_percent)
    """
    record = SeqIO.read(fasta_path, "fasta")
    sequence = record.seq.upper()
    gc_values = []

    for i in range(0, len(sequence), window_size):
        window_seq = sequence[i:i + window_size]
        gc = gc_fraction(window_seq) * 100
        gc_values.extend([gc] * len(window_seq))  # Repeat value per base

    return gc_values  # <-- Only the list of floats