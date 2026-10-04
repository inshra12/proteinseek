from proteinseek.search.seeds import find_seeds

def test_find_seeds():
    database = {
        "protein_1": "MKTLLAAGV",
        "protein_5": "LLAAGVTP"
    }

    result = find_seeds("MKTLLAAGV", database, 4)

    assert ("LAAG", 4, "protein_1", 4) in result
    assert ("LAAG", 4, "protein_5", 1) in result