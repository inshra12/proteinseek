from proteinseek.io.fasta import read_fasta
def brute_force(filename,query):
    database = read_fasta(filename)
    for name,seq in database.items():
        if query == seq:
            return name,seq
    return None
