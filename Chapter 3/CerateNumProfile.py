def CerateNumProfile(Profile):
    '''Given a letter profile, create its probability-profile'''
    
    prof_row = [0 for i in range(len(Profile[0]))]
    numProfile = {'A': prof_row+[], 'C': prof_row+[],
                  'G': prof_row+[], 'T': prof_row+[]}
    for j in range(len(Profile[0])):
        for i in range(len(Profile)):
            letter = Profile[i][j]
            numProfile[letter][j] += 1. / len(Profile)
    
    return numProfile
    