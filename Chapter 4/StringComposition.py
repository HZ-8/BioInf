def StringComposition(Text, k):
    '''Split Text to a set of k-mers, overlapping in k-1 positions'''
    result = []
    for i in range(len(Text)-k+1):
        result.append(Text[i:i+k])
    result.sort()
    
    return result
    
def StringSpell(Patterns):
    '''merge Patterns to a single string; overlaping in k-1 positions'''
    result = Patterns[0]
    
    for i in range(1, len(Patterns)):
        result = result + Patterns[i][-1]
        
    return result

def PatternOverlap(string1, string2):
    '''boolean function returning True 
    if 2 k-strings overlap in k-1 positions'''
    result = False
    if string1[1:] == string2[:-1]:
        result = True
    return result
    
def OverlapGraph(Patterns):
    '''Create adjacency list from set of Patterns'''
    graph = []
    
    for i in range(len(Patterns)):
        for j in range(len(Patterns)):
            if i == j:
                continue
            if PatternOverlap(Patterns[i], Patterns[j]):
                graph.append([Patterns[i], Patterns[j]])
    
    return graph

def DeBruijn(k, Text):
    '''Glue repeated overlapping k-1 nodes of the adjacency graph'''
    graph = {}
    k = k-1
    
    for i in range(len(Text)-k):
        key = Text[i:i+k]
        if key in graph:
            graph[key].append(Text[i+1:i+1+k])
        else:
            graph[key] = [Text[i+1:i+1+k]]
    
    '''result = []
    for el in graph:
        result.append([el, graph[el]])
    result.sort()'''
    return graph   

def DeBruijnFromPatterns(Patterns):
    '''Glue repeated overlapping nodes of the adjacency graph'''
    graph = {}
    
    for pat in Patterns:
        pref = pat[:-1]
        suff = pat[1:]
        if pref in graph:
            graph[pref].append(suff)
        else:
            graph[pref] = [suff]
    
    '''result = []
    for el in graph:
        result.append([el, graph[el]])
    result.sort()'''
    return graph    
    
def PairedComposition(k, d, Text):
    '''Break Text to (k, d) pairs. Sort alphabetically'''
    result = []
    for i in range(len(Text)-2*k-d+1):
        result.append([Text[i:i+k], Text[i+k+d:i+2*k+d]])
    result.sort()
    
    return result

def StringSpelledByPairs(Patterns, d):
    '''Given a collection of (k, d) pairs, recunstruct a string that
    they were decomposed from, if one exists'''
    
    k = len(Patterns[0][0])
    first_pat = []
    second_pat = []
    for i in range(len(Patterns)):
        first_pat.append(Patterns[i][0])
        second_pat.append(Patterns[i][1])
    
    pref = StringSpell(first_pat)
    suff = StringSpell(second_pat)
    
    for i in range(k+d, len(pref)):
        if pref[i] <> suff[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    result = pref + suff[-k-d:]
    return result
    
def DeBruijnFromPatternsPairs(Patterns):
    '''Glue repeated overlapping nodes of the adjacency graph'''
    graph = {}
    
    for pat in Patterns:
        pref = pat[0][:-1] + pat[1][:-1]
        suff = pat[0][1:] + pat[1][1:]
        if pref in graph:
            graph[pref].append(suff)
        else:
            graph[pref] = [suff]
    
    '''result = []
    for el in graph:
        result.append([el, graph[el]])
    result.sort()'''
    return graph    