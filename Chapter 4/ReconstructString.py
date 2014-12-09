from StringComposition import DeBruijnFromPatterns
from BinaryMethods import KBinarySet

def EulerianCycle(AdjList):
    '''Make up an Eulerian graph from the adjacency list'''
    
    node = AdjList.keys()[0]
    eustr = [node]

    while AdjList <> {}:
        #in current path, define a node with unused exits
        for iter_node in eustr:
            if iter_node in AdjList:
                node = iter_node * 1
                break
       
       #reform the path to start and end in the node with an exit
        new_eustr = []
        pos = eustr.index(node)
        for i in range(pos, len(eustr)-1):
            new_eustr.append(eustr[i])
        for i in range(0, pos):
            new_eustr.append(eustr[i])  
        eustr = new_eustr + [node]
        
        #starting in the last node, exit it and continue walking the graph
        while node in AdjList:
            eustr.append(AdjList[node][0])
            new_node = AdjList[node][0] * 1
            AdjList[node].remove(AdjList[node][0])
            if AdjList[node] == []:
                del AdjList[node]
            node = new_node * 1

    return eustr

def EulerianPath(AdjList):
    '''Make up Euler path in graph'''
    
    #Find Start and End nodes of the path
    nodes = {}
    for key in AdjList:
        for value in AdjList[key]:
            if value in nodes:
                nodes[value] += 1
            else:
                nodes[value] = 1
            if key in nodes:
                nodes[key] -= 1
            else:
                nodes[key] = -1

    for key in nodes:
        if nodes[key] == 1:
            end_node = key
        if nodes[key] == -1:
            start_node = key
    
    #Add an edge from end to start node
    if end_node in AdjList:
        AdjList[end_node].append(start_node)
    else:
        AdjList[end_node] = [start_node]
    
    #Find Eulerian Cycle in new AdjList
    cycle = EulerianCycle(AdjList)
    
    #Rearrange the cycle to start in start_node and end in end_node
    i = 0
    found = False
    while not found:
        pos = cycle.index(end_node, i)
        if pos == len(cycle):
            j = 0
        else:
            j = pos + 1
        if cycle[j] == start_node:
            found = True
        else:
            i = pos + 1
    
    eu_path = []
    for i in range(j, len(cycle)-1):
        eu_path.append(cycle[i])
    for i in range(0, j):
        eu_path.append(cycle[i])
    
    return eu_path
    
def StringReconstruction(Patterns):
    '''Given an integer k and a list of k-mers Patterns,
    reconstruct the genome (one of possible)'''
    
    AdjList = DeBruijnFromPatterns(Patterns)
    genome = EulerianPath(AdjList)
    
    return genome

def KUniversalCircularString(k):
    '''From k, create any binary k-universal string'''
    patterns = KBinarySet(k)
    AdjList = DeBruijnFromPatterns(patterns)
    k_univ_str = EulerianCycle(AdjList)
    k_univ_str = k_univ_str[:-k+1]
    
    return k_univ_str