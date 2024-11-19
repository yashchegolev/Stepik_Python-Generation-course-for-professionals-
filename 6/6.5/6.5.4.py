def wins(pairs):
    from collections import defaultdict
    result = defaultdict(set)
    for pair in pairs:
        result[pair[0]].add(pair[1])
    return result
