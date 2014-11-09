import PatternToNumber as p_n

def FindClump(Genome, k, L, t):
    '''In Genome, find (L, t) clumps of k-mers. Returns list of k-mers'''
    clumps = [] #list of clumping k-mers
    KMerPos = [[]]* (4 ** k) # form a list for positions of all k-mers
    for i in range(len(Genome) - k + 1):
        #get current k-mer and its index in list 
        Pattern =  Genome[i: i + k]
        j = p_n.PatternToNumber(Pattern) 
        #if current k-mer already contains t positions withing L, then skip
        if len(KMerPos[j]) == t:
            continue
        
        #there are less than t positions; add the next one to list
        KMerPos[j] = KMerPos[j] + [i]
        #let's see if current set of positions is within L
        dist = KMerPos[j][-1] + k - KMerPos[j][0]
        
        #the last position spreads beyond L, then delete the 1st position
        while dist > L:
            KMerPos[j].remove(KMerPos[j][0])
            dist = KMerPos[j][-1] + k - KMerPos[j][0]
                
        #okay, now at index i, we have a list of positions within L
        if len(KMerPos[j]) == t:
            clumps.append(Pattern)
            
    return clumps