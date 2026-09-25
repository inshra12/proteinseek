# # stores each k-mer in a dictionary along with the protein name and position
from proteinseek.io.fasta import read_fasta
def kmer_index(database,k):
    index = {}
    for protein,seq in database.items():
        for i in range(len(seq)-k+1):
            window = seq[i:k+i]
            if window in index:
                index[window].append((protein,i))
            else:
                index[window] = [(protein,i)]
    return index

# database = read_fasta("../../../data/small/proteins.fasta")
# print(kmer_index(database,4))
        



    




