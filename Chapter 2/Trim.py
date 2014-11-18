import LinearScore as ls, LetterPeptideToNum as ltn

def NumTrim(numLeaderboard, Spectrum, N):
    '''In a list of peptides Leaderboard, take only N (with ties) of 
    top-rating ones in scope of matching Spectrum'''
    if numLeaderboard == []:
        return numLeaderboard
        
    LinearScores = []
    
    for j in range(len(numLeaderboard)):
        numPept = numLeaderboard[j]
        LinearScores.append(ls.LinearScore(numPept, Spectrum))

    LinearScores, numLeaderboard = (list(t) for t in
                  zip(*sorted(zip(LinearScores, numLeaderboard), reverse = True)))    
    new_board = numLeaderboard[:N]
    
    i = N
    while (i < len(numLeaderboard)) and (LinearScores[i] == LinearScores[N-1]):
        new_board.append(numLeaderboard[i])
        i += 1
    
    numLeaderboard = new_board
    
    return numLeaderboard


def Trim(Leaderboard, Spectrum, N, MassDict):
    '''In a list of peptides Leaderboard, take only N (with ties) of 
    top-rating ones in scope of matching Spectrum
    massDict is 20-elem size'''
    LinearScores = []
    
    for j in range(len(Leaderboard)):
        Peptide = Leaderboard[j]
        numPept = ltn.LetterPeptideToNum(Peptide, MassDict)
        LinearScores.append(ls.LinearScore(numPept, Spectrum))
    
    LinearScores, Leaderboard = (list(t) for t in
                  zip(*sorted(zip(LinearScores, Leaderboard), reverse = True)))    
    new_board = Leaderboard[:N]
    
    i = N
    while (i < len(Leaderboard)) and (LinearScores[i] == LinearScores[N-1]):
        new_board.append(Leaderboard[i])
        i += 1
    
    Leaderboard = new_board
    
    return Leaderboard