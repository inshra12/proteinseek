def get_kmers(sequence, k):
    k_mers = []
    for i in range(len(sequence)-k+1):
        window = sequence[i:k+i]
        k_mers.append(window)
    return k_mers

result = get_kmers("MKTLLAAGV", 4)
print(result)

