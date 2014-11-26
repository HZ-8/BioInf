from ProfileMostProbableKMer import ProfileMostProbableKMer
from CreateNumProfile import CreateNumProfile
from Score import Score
from random import randrange

def GreedyMotifSearch(DNA, k, t):
    BestMotifs = []
    for string in DNA:
        BestMotifs.append(string[:k])
    
    for i in range(len(DNA[0])-k+1):
        Motifs = [DNA[0][i:i+k]]
        
        for j in range(1,t):
            Profile = CreateNumProfile(Motifs, 1)
        
            Motifs.append(ProfileMostProbableKMer(DNA[j], k, Profile))
        
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        
    return BestMotifs
    
def RandomizedMotifSearch(DNA, k, t):
    Motifs = []
    for string in DNA:
        index = randrange(len(string)-k+1)
        Motifs.append(string[index:index+k])
    
    BestMotifs = Motifs
    while True:
        Profile = CreateNumProfile(Motifs, 1)
        
        Motifs = []
        for i in range(0,t):
            Motifs.append(ProfileMostProbableKMer(DNA[i], k, Profile))
         
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        else:
            return BestMotifs, Score(BestMotifs)