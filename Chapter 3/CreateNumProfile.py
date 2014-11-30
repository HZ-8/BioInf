def CreateNumProfile(Motifs, AddCoeff = 0):
    '''Given a set of letter motifs, create its probability-profile'''
    zero_row = [0 for i in range(len(Motifs[0]))]
    numProfile = {'A': zero_row+[], 'C': zero_row+[],
                  'G': zero_row+[], 'T': zero_row+[]}
    
    for j in range(len(Motifs[0])):
        for i in range(len(Motifs)):
            letter = Motifs[i][j]
            numProfile[letter][j] += 1. / len(Motifs)
    
    if AddCoeff == 0:
        return numProfile
        
    for key in numProfile:
        for i in range (len(numProfile[key])):
            numProfile[key][i] += float(AddCoeff) / len(Motifs)
    
    return numProfile