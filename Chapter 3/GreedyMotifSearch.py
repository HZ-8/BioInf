from ProfileMostProbableKMer import ProfileMostProbableKMer

def GreedyMotifSearch(DNA, k, t):
    BestMotifs = []
    for string in DNA:
        BestMotifs.append(string[:k])
    
    for i in range(len(DNA[0])-k+1):
        Motifs = []
        Motifs[0] = DNA[0][i:i+k]
        
        for j in range(2,t):
            Profile = []
            for l in range(j):
                Profile[l] = Motifs[l]
            Motifs[j] = ProfileMostProbableKMer(DNA[j], k, Profile)
        
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        
    return BestMotifs