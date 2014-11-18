import Neighbors as nb, ApproximatePatternCount as apc

def MotifEnumeration(DNA, k, d):
    '''Given a collection of strings DNA and an integer d, a k-mer is
    a (k,d)-motif if it appears in every string from DNA with at most
    d mismatches. Return all (k,d) mootifs'''
    
    Motifs = set()
    Patterns = set()
    neibhood = set()
    for string in DNA:
        for i in range (len(string) - k + 1):
            pattern = string[i: i+k]
            Patterns.add(pattern)
            neibs = nb.Neighbors(pattern, d)
            for neib in neibs:
                neibhood.add(neib)
    #print neibhood
    for neib in neibhood:
        found_in_all = True
        for string in DNA:
            found = False
            if apc.ApproximatePatternCount(string, neib, d) > 0:
                found = True
            found_in_all = found_in_all and found
        if found_in_all:
            Motifs.add(neib)
    
    return Motifs
            
            
