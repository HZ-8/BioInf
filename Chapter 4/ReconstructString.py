def EulerianCycle(AdjList):
    '''Make up an Eulerian graph from the adjacency list'''
    
    start_node = AdjList.keys()[0]
    eustr = []
    
    while AdjList <> {}:
        for node in eustr:
            if node in AdjList:
                start_node = node + ''
                break
        new_eustr = []
        if eustr <> []:
            pos = eustr.index(start_node)
            for i in range(pos, len(eustr)):
                new_eustr.append(eustr[i])
            for i in range(0, pos):
                new_eustr.append(eustr[i])
        
        node = new_eustr[len(new_eustr)]
        while node in AdjList:
            new_eustr.append(AdjList[node][0])
            AdjList[node].remove(AdjList[node][0])
            if AdjList[node] == []:
                del AdjList[node]
        
        eustr = new_eustr + []
    
    return eustr