from proteinseek.indexing.kmers import get_kmers


def test_get_kmers():
    result = get_kmers("MKTLLAAGV", 4)

    assert result == [
        "MKTL",
        "KTLL",
        "TLLA",
        "LLAA",
        "LAAG",
        "AAGV"
    ]