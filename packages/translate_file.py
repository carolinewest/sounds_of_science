from Bio import SeqIO
from Bio.Seq import Seq

def read_fasta(filename):
    """Reads a FASTA file and returns a list of SeqRecord objects."""
    records = []
    with open(filename, "r") as file:
        for sequence in SeqIO.parse(file, "fasta"):
            records.append(sequence)
    return records

def translate_file(file):

    """Takes in a FASTA file and returns a single string with all the translated records."""
    
    #FastA File read call
    sequences = read_fasta(file)

    #Empty string setup
    translatedsequences = ''

    #Interates through all the seqrecords, translates the sequences, and makes a cumulated string of all the amino acids
    for seq in sequences:
        seq =str(seq.seq)
        if len(seq)%3==1:
            seq+="NN"
        elif len(seq)%3==2:
            seq+="N"

        translation = str((Seq(seq)).translate(to_stop=False))

        #Cumulated string of all the sequences
        translatedsequences += translation
        
        #Returns the string
    return translatedsequences

