def similarity_score(query, target):
    if not query or not target:
        return 0.0
    count = 0
    for q,t in zip(query, target):
        if q == t:
            count += 1
    return count/min(len(query), len(target))

def score_candidates(query, database, candidates):
    scores = []

    for candidate in candidates:
        protein, diagonal = candidate

        target = database[protein]

        score = similarity_score(query, target)

        scores.append((protein, score))
        scores.sort(key=lambda x: x[1], reverse=True)

    return scores