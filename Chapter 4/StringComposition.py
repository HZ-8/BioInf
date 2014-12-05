def StringComposition(Text, k):
    result = []
    for i in range(len(Text)-k+1):
        result.append(Text[i:i+k])
    result.sort()
    
    return result
    
def StringSpell(Patterns):
    result = Patterns[0]
    
    for i in range(1, len(Patterns)):
        result = result + Patterns[i][-1]
        
    return result

def PatternOverlap(string1, string2):
    result = False
    if string1[1:] == string2[:-1]:
        result = True
    return result
    
def OverlapGraph(Patterns):
    graph = []
    
    for i in range(len(Patterns)):
        for j in range(len(Patterns)):
            if i == j:
                continue
            if PatternOverlap(Patterns[i], Patterns[j]):
                graph.append([Patterns[i], Patterns[j]])
    
    return graph