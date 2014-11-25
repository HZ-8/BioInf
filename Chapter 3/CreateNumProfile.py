def CreateNumProfile(Profile, AddCoeff = 0):
    '''Given a letter profile, create its probability-profile'''
    zero_row = [0 for i in range(len(Profile[0]))]
    numProfile = {'A': zero_row+[], 'C': zero_row+[],
                  'G': zero_row+[], 'T': zero_row+[]}
    
    for j in range(len(Profile[0])):
        for i in range(len(Profile)):
            letter = Profile[i][j]
            numProfile[letter][j] += 1. / len(Profile)
    
    if AddCoeff == 0:
        return numProfile
        
    for key in numProfile:
        for i in range (len(numProfile[key])):
            numProfile[key][i] += float(AddCoeff) / len(Profile)
    
    return numProfile