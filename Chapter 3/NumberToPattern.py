def NumberToPattern(pos, k):
    gene_alph = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    rem = pos
    Pattern = ''
    while rem > 0:
        pos = rem % 4
        Pattern = gene_alph[pos] + Pattern
        rem = rem // 4
    if len(Pattern) < k:
        Pattern = 'A' * (k - len(Pattern)) + Pattern
    return Pattern