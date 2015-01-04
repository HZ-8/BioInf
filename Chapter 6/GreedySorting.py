def ReverseSort(P, k):
    p1 = P[:k-1]
    
    p2 = []
    for el in P:
        p2.append(abs(el))
        
    pos = p2.index(k)
    rev = P[k-1:pos+1]
    rev = rev[::-1]
    for el in rev:
        p1.append(-el)
    
    p1 += P[pos+1:]
    
    return p1
    

def GreedySorting(P):
    '''Given a permutation P, output the sequence of permutations ending with
     the identity permutation'''
     
    dist = 0
    rev = []
    
    for k in range(len(P)):

        if abs(P[k]) <> k+1:
            P = ReverseSort(P, k+1)
            rev.append(P*1)
            dist += 1
        if P[k] == -(k+1):
            P[k] = -P[k]
            rev.append(P*1)
            dist += 1
    return dist, rev