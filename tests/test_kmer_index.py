from proteinseek.indexing.kmer_index import kmer_index
from proteinseek.io.fasta import read_fasta


def test_get_kmer_index():
    database = read_fasta("data/small/proteins.fasta")

    result = kmer_index(database, 4)

    assert result["LAAG"] == [
        ("protein_1", 4),
        ("protein_5", 1)
    ]

def test_repeated_kmer():
    database = {
        "protein_x": "MPLWMPLW"
    }

    result = kmer_index(database, 4)

    assert result["MPLW"] == [
        ("protein_x", 0),
        ("protein_x", 4)
    ]