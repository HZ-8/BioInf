from HammingDistance import HammingDistance
from NumberToPattern import NumberToPattern

def DistanceBetweenPatternAndStrings(Pattern, DNA):
    '''compute d(Pattern, Dna), the sum of distances
    between Pattern and each string in Dna = {Dna1, ..., Dnat}.'''
    
    k = len(Pattern)
    distance = 0
    
    for Text in DNA:
        min_ham_dist = k+1
        for i in range(len(Text)-k+1):
            k_mer = Text[i:i+k]
            temp_dist = HammingDistance(Pattern, k_mer)
            if temp_dist < min_ham_dist:
                min_ham_dist = temp_dist
        distance = distance + min_ham_dist
        
    return distance
    
def MedianString(DNA, k):
    '''Of all possible k-mers, find the one minimizing Hamming distance 
    between it and potential motifs in each string of DNA'''
    
    distance = k*len(DNA)+1
    Median = ''
    for i in range(4**k):
        Pattern = NumberToPattern(i, k)
        temp_dist = DistanceBetweenPatternAndStrings(Pattern, DNA)
        if distance > temp_dist:
            distance = temp_dist
            Median = Pattern

    return Median