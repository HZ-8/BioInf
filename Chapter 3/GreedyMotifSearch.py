from ProfileMostProbableKMer import ProfileMostProbableKMer
from CreateNumProfile import CreateNumProfile
from Score import Score

def GreedyMotifSearch(DNA, k, t):
    BestMotifs = []
    for string in DNA:
        BestMotifs.append(string[:k])
    
    for i in range(len(DNA[0])-k+1):
        Motifs = [DNA[0][i:i+k]]
        
        for j in range(1,t):
            Profile = CreateNumProfile(Motifs)
        
            Motifs.append(ProfileMostProbableKMer(DNA[j], k, Profile))
        
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        
    return BestMotifs