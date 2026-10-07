# ProteinSeek

ProteinSeek is a small educational protein sequence search project I built to practice data structures, algorithms, and computational problem-solving in a bioinformatics setting.

The project explores a simplified search pipeline using:

* FASTA parsing
* K-mer generation and indexing
* Seed search
* Diagonal detection
* Candidate prefiltering
* Simple similarity scoring

The main idea is to understand how indexing and filtering can reduce repeated database scanning and improve search efficiency.

The project was inspired by studying the general ideas behind fast protein sequence search tools such as **MMseqs2**, but ProteinSeek is **not a reimplementation or clone** of MMseqs2.

## Current Status

The core search pipeline is implemented and tested with `pytest`. I am also experimenting with benchmarking the brute-force and indexed approaches to understand their time and space trade-offs.

## Running Tests

```bash
pytest
```

This is primarily a learning and portfolio project, with future improvements focused on benchmarking, optimization, and more realistic sequence scoring.
