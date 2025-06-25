#!/usr/bin/env python3
import pandas as pd

def map_pitch(aa_sequence):
    """
    Identifies non-overlapping open reading frames (ORFs) in an amino acid sequence.
    An ORF starts with 'M' and ends with '*', with no '*' in between.
    """
    orfs = []
    used_positions = set()
    i = 0

    while i < len(aa_sequence):
        if aa_sequence[i] == 'M' and i not in used_positions:
            for j in range(i + 1, len(aa_sequence)):
                if aa_sequence[j] == '*':
                    if '*' not in aa_sequence[i+1:j]:
                        # Check if any position in this ORF is already used
                        if not any(pos in used_positions for pos in range(i, j+1)):
                            orfs.append((i, j))
                            used_positions.update(range(i, j+1))  # Mark as used
                            i = j  # Jump to end of this ORF
                    break
        i += 1

    return orfs