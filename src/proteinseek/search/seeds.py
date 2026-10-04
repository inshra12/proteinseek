from proteinseek.indexing.kmer_index import kmer_index
from proteinseek.io.fasta import read_fasta
# database = read_fasta("../../../data/small/proteins.fasta")

def  find_seeds(q,database,k):
    seeds = []

    index = kmer_index(database, k)

    for i in range(len(q) - k + 1):
        window = q[i:i+k]

        if window in index:
            for protein, position in index[window]:
                seeds.append((window, i, protein, position))

    return seeds
    

# print(query("MKTLLAAGV",4))
# query = "MKTLLAAGV"
# k = 4
# for i in range(len(query)-k+1):
#     window = query[i:k+i]
#     print(window,i)
# def query()