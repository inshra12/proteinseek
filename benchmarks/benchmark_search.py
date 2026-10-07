import random
import time
from proteinseek.baseline.brute_force import brute_force
from proteinseek.indexing.kmer_index import kmer_index
from proteinseek.search.seeds import find_seeds
from proteinseek.search.diagonals import group_diagonals
from proteinseek.search.prefilter import prefilter
from proteinseek.scoring.alignment import score_candidates


def generate_database(num_proteins, sequence_length):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    database = {}

    random.seed(42)

    for i in range(num_proteins):
        sequence = ""

        for _ in range(sequence_length):
            sequence += random.choice(amino_acids)

        database[f"protein_{i}"] = sequence

    return database
    

# def write_fasta(database, filename):
#     with open(filename, "w") as file:
#         for protein, sequence in database.items():
#             file.write(f">{protein}\n")
#             file.write(f"{sequence}\n")

# database = generate_database(1000, 100)
# write_fasta(database, "data/benchmark/proteins.fasta")

database = generate_database(1000, 100)
query = database["protein_999"]

start = time.perf_counter()

result = brute_force(
    "data/benchmark/proteins.fasta",
    query
)

end = time.perf_counter()

print("Result:", result[0])
print("Brute-force time:", end - start)

k = 4

index_start = time.perf_counter()

index = kmer_index(database, k)

index_end = time.perf_counter()

start = time.perf_counter()

seeds = find_seeds(query, index, k)
groups = group_diagonals(seeds)
candidates = prefilter(groups, 3)
scores = score_candidates(query, database, candidates)

end = time.perf_counter()

print("Index construction time:", index_end - index_start)
print("Search time:", end - start)
print("Candidates:", len(candidates))