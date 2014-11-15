import LinearScore as ls, FrequentElements as fel

def NumTrim_2(numLeaderboard, Spectrum, N):
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