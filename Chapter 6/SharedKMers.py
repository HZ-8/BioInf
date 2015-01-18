def ComplementPattern(Pattern):
    '''This proceduer returns a complementary sting in reverse order for the
    given string sequence'''
    gene_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    compl = ''
    for letter in Pattern:
        compl = gene_dict[letter] + compl
    return compl

def MakeDictFromString(k, S, reverse):
    d = {}
    for i in range(len(S) -k+1):
        block = S[i: i+k]
        if reverse:
            j = len(S)-i-k
        else:
            j = i
        if block in d:
            d[block].append(j)
        else:
            d[block] = [j]
    return d

def SharedKMersList(k, G1, G2):
    '''Return list of k-mers shared by 2 genomes G1 and G2, or by their 
    reberse complements. Return coordinate pairs'''
    complG1 = ComplementPattern(G1)
    complG2 = ComplementPattern(G2)   
    
    d1 = MakeDictFromString(k, G1, False)
    d2 = MakeDictFromString(k, complG1, True)
    d3 = MakeDictFromString(k, G2, False)
    d4 = MakeDictFromString(k, complG2, True)
    
    shares = []
    '''print G1
    print d1
    print complG1
    print d2
    print G2
    print d3
    print complG2
    print d4'''
    
    for el in d1:
        if el in d3:
            for i in d1[el]:
                for j in d3[el]:
                    if (i, j) not in shares:
                        shares.append((i, j))
                        #print 1, i, j, el
        if el in d4:
            for i in d1[el]:
                for j in d4[el]:
                    if (i, j) not in shares:
                        shares.append((i, j))
                        #print 2, i, j, el
    for el in d2:
        if el in d3:
            for i in d2[el]:
                for j in d3[el]:
                    if (i, j) not in shares:
                        shares.append((i, j))
                        #print 3, i, j, el

    return shares