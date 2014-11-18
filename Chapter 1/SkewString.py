def SkewString(Genome):
    '''For given Genome string, return string of same length, 
    each element of which is a skew number at this position'''
    skew = [0]
    for i in range(len(Genome)):
        temp_skew = skew[i]
        if Genome[i] == 'C':
            temp_skew -=1
        if Genome[i] == 'G':
            temp_skew +=1
        skew.append(temp_skew)
    return skew
    