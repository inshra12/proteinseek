def prefilter(groups, min_seeds):
    candidates = {}

    for key, count in groups.items():
        if count >= min_seeds:
            candidates[key] = count

    return candidates