from proteinseek.io.fasta import read_fasta

def test_read_fasta():
    result = read_fasta("data/small/proteins.fasta")

    assert result["protein_1"] == "MKTLLAAGV"
    assert result["protein_2"] == "GAVLKDPN"