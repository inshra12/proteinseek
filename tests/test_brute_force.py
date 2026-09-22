from proteinseek.baseline.brute_force import brute_force
def test_brute_force():
    result = brute_force("data/small/proteins.fasta", "MKTLLAAGV")
    assert result == ("protein_1", "MKTLLAAGV")

def test_brute_force_no_match():
    result = brute_force("data/small/proteins.fasta", "AAAAAAA")

    assert result is None