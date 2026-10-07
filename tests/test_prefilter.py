from proteinseek.search.prefilter import prefilter


def test_prefilter():
    groups = {
        ("protein_1", 0): 4,
        ("protein_5", -3): 2,
        ("protein_2", 7): 1
    }

    result = prefilter(groups, 3)

    assert result == {
        ("protein_1", 0): 4
    }