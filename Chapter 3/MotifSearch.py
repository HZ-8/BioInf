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
            Profile = CreateNumProfile(Motifs, 1)
        
            Motifs.append(ProfileMostProbableKMer(DNA[j], k, Profile))
        
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        
    return BestMotifs
    
def RandomizedMotifSearch(DNA, k, t):
    Motifs = []
    for string in DNA:
        
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string
            from Dna
        BestMotifs ← Motifs
        while forever
            Profile ← Profile(Motifs)
            Motifs ← Motifs(Profile, Dna)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
            else
                return BestMotifs