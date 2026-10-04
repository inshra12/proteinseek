from proteinseek.search.diagonals import calculate_diagonal,group_diagonals


def test_calculate_diagonal():
    seed = ("LAAG", 4, "protein_1", 4)

    result = calculate_diagonal(seed)

    assert result == 0

def test_calculate_nonzero_diagonal():
    seed = ("LAAG", 4, "protein_5", 1)

    result = calculate_diagonal(seed)

    assert result == -3

def test_group_diagonals():
    seeds = [
        ("MKTL", 0, "protein_1", 0),
        ("KTLL", 1, "protein_1", 1),
        ("TLLA", 2, "protein_1", 2),
        ("LLAA", 3, "protein_1", 3),
        ("LAAG", 4, "protein_5", 1),
        ("AAGV", 5, "protein_5", 2),
    ]

    result = group_diagonals(seeds)

    assert result[("protein_1", 0)] == 4
    assert result[("protein_5", -3)] == 2