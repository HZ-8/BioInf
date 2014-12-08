def EulerianCycle(AdjList):
    '''Make up an Eulerian graph from the adjacency list'''
    
    node = AdjList.keys()[0]
    eustr = [node]

    while AdjList <> {}:
        #in current path, define a node with unused exits
        for iter_node in eustr:
            if iter_node in AdjList:
                node = iter_node + 0
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
            new_node = AdjList[node][0] + 0
            AdjList[node].remove(AdjList[node][0])
            if AdjList[node] == []:
                del AdjList[node]
            node = new_node + 0

    return eustr