def PatternToNumber(Pattern):
    gene_alph = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    pos = 0
    for i in range(len(Pattern)):
        pos = pos + 4 ** (len(Pattern)-i-1) * gene_alph[Pattern[i]]
    return pos
        