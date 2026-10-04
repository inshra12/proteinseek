def calculate_diagonal(seed):
    kmer, query_position, protein, target_position = seed

    return target_position - query_position



def group_diagonals(seeds):
    groups = {}

    for seed in seeds:
        kmer, query_position, protein, target_position = seed

        diagonal = target_position - query_position

        key = (protein, diagonal)

        if key in groups:
            groups[key] += 1
        else:
            groups[key] = 1

    return groups

seed = ("LAAG", 4, "protein_1", 3)

print(calculate_diagonal(seed))
