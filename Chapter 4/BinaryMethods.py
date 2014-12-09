def KBinarySet(k):
    '''Return a list of all possible k-length binary strings'''
    
    bink = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(k)]))


    binlist = []
    for i in range(2 ** k):    
        s = bink(i)
        binlist.append(s)
    
    binlist.sort()
    return binlist