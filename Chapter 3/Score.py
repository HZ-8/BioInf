def Score(Motifs):
    '''Given a set of motif strings, calculate score'''
    
    score = 0
    zero_row = [0 for i in range(len(Motifs[0]))]
    counts = {'A': zero_row+[], 'C': zero_row+[],
                  'G': zero_row+[], 'T': zero_row+[]}
    
    for j in range(len(Motifs[0])):
        for i in range(len(Motifs)):
            letter = Motifs[i][j]
            counts[letter][j] += 1
        
        score = score + counts['A'][j] + counts['C'][j] + counts['G'][j] + \
        counts['T'][j] - \
        max(counts['A'][j], counts['C'][j], counts['G'][j], counts['T'][j])
        
    return score