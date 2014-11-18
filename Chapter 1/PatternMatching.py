def PatternMatching(Pattern, Genome):
    pos = []
    k = len(Pattern)
    for i in range(len(Genome) - k + 1):
        if Genome[i: i + k] == Pattern:
            pos.append(i)
    return pos