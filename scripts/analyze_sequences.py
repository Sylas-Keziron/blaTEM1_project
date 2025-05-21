from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Load sequences
fasta_file = "./data/blatem1_hits.fasta"
sequences = list(SeqIO.parse(fasta_file, "fasta"))

print(f"Loaded {len(sequences)} sequences from {fasta_file}\n")

for record in sequences:
    seq_id = record.id
    seq_len = len(record.seq)
    seq_gc = round(gc_fraction(record.seq) * 100, 2)
    protein_seq = record.seq.translate(to_stop=True)

    print(f"> {seq_id}")
    print(f"Length: {seq_len} bp")
    print(f"GC content: {seq_gc}%")
    print(f"First 30 aa (protein): {protein_seq[:30]}")
    print("-" * 40)
