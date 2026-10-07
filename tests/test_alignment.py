from proteinseek.scoring.alignment import score_candidates,similarity_score


def test_score_candidates():
    query = "MKTLL"
    database = {
        "protein_1": "MKTLL",
        "protein_2": "MKTAL"
    }

    candidates = {
        ("protein_1", 0): 4,
        ("protein_2", 0): 3
    }

    result = score_candidates(query, database, candidates)

    assert ("protein_1", 1.0) in result
    assert ("protein_2", 0.8) in result

def test_similarity_score_empty():
    result = similarity_score("", "MKTLL")
    assert result == 0.0