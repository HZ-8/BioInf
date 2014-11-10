import LinearScore as ls, LetterPeptideToNum as ltn

def Trim(Leaderboard, Spectrum, N, MassDict):
    '''In a list of peptides Leaderboard, take only N (with ties) of 
    top-rating ones in scope of matching Spectrum'''
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