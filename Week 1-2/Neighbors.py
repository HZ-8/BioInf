import HammingDistance as hd
gene_alph = ['A', 'C', 'G', 'T']

def ImmediateNeighbors(Pattern):
    neibhood = {Pattern}
    for i in range(len(Pattern)):
        let = Pattern[i]
        for nucl in gene_alph:
            if let != nucl:
                neib = Pattern[:i] + nucl + Pattern[i+1:]
                neibhood.add(neib)
    return neibhood

def Neighbors(Pattern, d):
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neibhood = []
    suff = Pattern[1:]
    suffneibhood = Neighbors(suff, d)
    for sneib in suffneibhood:
        if hd.HammingDistance(suff, sneib) < d:
            for nucl in gene_alph:
                neib = nucl + sneib
                neibhood.append(neib)
        else:
            neib = Pattern[0] + sneib
            neibhood.append(neib)
    return neibhood   
    
def ExNeighbors(Pattern, d, rem):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neibhood = []
    suff = Pattern[1:]
    suffneibhood = ExNeighbors(suff, d, rem-1)
    for sneib in suffneibhood:
        if hd.HammingDistance(suff, sneib) < d:
            for nucl in gene_alph:
                neib = nucl + sneib
                td = hd.HammingDistance(neib, Pattern[0] + sneib) + rem
                if td >= d:
                    neibhood.append(neib)
        else:
            neib = Pattern[0] + sneib
            neibhood.append(neib)
    return neibhood