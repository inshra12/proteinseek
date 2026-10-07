from proteinseek.search.seeds import find_seeds
from proteinseek.indexing.kmer_index import kmer_index


def test_find_seeds():
    database = {
        "protein_1": "MKTLLAAGV",
        "protein_5": "LLAAGVTP"
    }

    index = kmer_index(database, 4)

    result = find_seeds("MKTLLAAGV", index, 4)

    assert ("LAAG", 4, "protein_1", 4) in result
    assert ("LAAG", 4, "protein_5", 1) in result