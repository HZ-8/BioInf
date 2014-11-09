import SkewString as ss
def MinimumSkew(Genome):
    '''In given Genome string, finds all positions, where Skew is minimal'''
    pos = []
    skew = ss.SkewString(Genome)
    min_skew = min(skew)
    for i in range(0, len(skew)):
        if skew[i] == min_skew:
            pos.append(i)
    
    return pos