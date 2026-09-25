# # generates k-mers
def get_kmers(sequence, k):
    k_mers = []
    for i in range(len(sequence)-k+1):
        window = sequence[i:k+i]
        k_mers.append(window)
        print(window,i)
    return k_mers


# print(get_kmers( "MKTLLAAGV",4))

