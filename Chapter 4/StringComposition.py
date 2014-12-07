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
    
    result = []
    for el in graph:
        result.append([el, graph[el]])
    result.sort()
    return result   

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
    
    result = []
    for el in graph:
        result.append([el, graph[el]])
    result.sort()
    return result    
    