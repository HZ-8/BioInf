def ChromosomeToCycle(Chromosome):
    '''Chromosome is a sequence of synteny blocks in format [-3, +1, +2]
    Return its representation of nodes [6, 5, 1, 2, 3, 4]'''
    nodes = []
    
    for el in Chromosome:
        if el > 0:
            nodes.append(el*2-1)
            nodes.append(el*2)
        else:
            nodes.append(-el*2)
            nodes.append(-el*2-1)
    return nodes
    
def CycleToChromosome(Nodes):
    '''An opposite procedure to the above one'''
    Chromosome = []
    
    for i in range(len(Nodes)/2):
        if Nodes[2*i] < Nodes[2*i+1]:
            Chromosome.append(Nodes[2*i+1]/2)
        else:
            Chromosome.append(-Nodes[2*i]/2)
    return Chromosome
    
def PairToBlock(Nodes):
    '''By pair of nodes return block number'''
    if Nodes[0] < Nodes[1]:
        block = Nodes[1]/2
    else:
        block = -Nodes[0]/2
    return block
    
def ColoredEdges(G):
    '''Given a genome G in format [+1, -2, -3], [+4, +5, -6], output 
    a collection of colored edges in its graph in format [2, 4], [3, 6],...'''
    edges = []
    
    for chromosome in G:
        nodes = ChromosomeToCycle(chromosome)
        
        for i in range(len(chromosome)-1):
            edges.append([nodes[2*i+1], nodes[2*i+2]])
        i = len(nodes)-1
        edges.append([nodes[i], nodes[0]])
    
    return edges

def ColoredEdgesGraph(G):
    '''Given a genome G in format [+1, -2, -3], [+4, +5, -6], output 
    a collection of colored edges in its graph in format
    {2: 4, 4: 2, 3:6],... Each non-directed edge is represented
    as 2 oppositly directed adges'''
    edges = {}
    
    for chromosome in G:
        nodes = ChromosomeToCycle(chromosome)
        
        for i in range(len(chromosome)-1):
            edges[nodes[2*i+1]] = nodes[2*i+2]
            edges[nodes[2*i+2]] = nodes[2*i+1]
        i = len(nodes)-1
        edges[nodes[i]] = nodes[0]
        edges[nodes[0]] = nodes[i]
    
    return edges

def GraphToGenome(Graph):
    '''From a graph, which is an array of edges, find its original genome
    as a sequence of synteny blocks'''
    
    G = []
    chromosome = []
    
    while len(Graph) > 0:
        if chromosome == []:
            curr_edge = Graph[0]
            new_edge = []
            Graph.remove(curr_edge)
            
            tail = curr_edge[0]
            if tail % 2 == 0:
                head = tail -1
            else:
                head = tail + 1    
            block = CycleToChromosome([head, tail])
            chromosome += block
            
        head = curr_edge[1]
        if head % 2 == 0:
            tail = head - 1
        else:
            tail = head + 1
        
        for edge in Graph:
            if edge[0] == tail:
                chromosome += CycleToChromosome([head, tail])
                new_edge = edge
                Graph.remove(edge)
                break
            if edge[1] == tail:
                chromosome += CycleToChromosome([head, tail])
                new_edge = [edge[1], edge[0]]
                Graph.remove(edge)
                break
            
        if new_edge == []: #cycle is done
            G.append(chromosome)
            chromosome = []
        else: #we found new edge in chain, add the synteny block
            curr_edge = new_edge * 1
            new_edge = []
    
    G.append(chromosome)
    
    return G

def GraphToGenomeGraph(Graph):
    '''From a graph, which is a dictionary of oppositely directed edges, 
    find its original genome as a sequence of synteny blocks'''
    
    G = []
    chromosome = []
    
    while len(Graph) > 0:
        if chromosome == []:
            index = Graph.keys()[0]
            curr_edge = [index, Graph[index]]
            Graph.pop(curr_edge[0])
            Graph.pop(curr_edge[1])
            
            tail = curr_edge[0]
            if tail % 2 == 0:
                head = tail -1
            else:
                head = tail + 1    
            block = PairToBlock([head, tail])
            chromosome.append(block)
            
        head = curr_edge[1]
        if head % 2 == 0:
            tail = head - 1
        else:
            tail = head + 1
    
        if tail in Graph:
            chromosome.append(PairToBlock([head, tail]))
            curr_edge = [tail, Graph[tail]]
            Graph.pop(curr_edge [0])
            Graph.pop(curr_edge [1])
            
        else:
            G.append(chromosome)
            chromosome = []
    
    if chromosome <> []:
        G.append(chromosome)
    
    return G
    
def BreakGraph(Graph, i1, i2, j1, j2):
    '''In Graph destroy edges i1-i2, j1-j2, and create i1-j1, i2-j2'''
    
    if [i1, i2] in Graph:
        Graph.remove([i1, i2])
    elif [i2, i1] in Graph:
        Graph.remove([i2, i1])
    if [j1, j2] in Graph:
        Graph.remove([j1, j2])
    elif [j2, j1] in Graph:
        Graph.remove([j2, j1])   
        
    Graph.append([i1, j1])
    Graph.append([i2, j2])
        
    return Graph
    
def BreakGenome(G, i1, i2, j1, j2):
    '''Given a genome (one chromosome) as a sequence of synteny blocks,
    return its broken version'''
    
    graph = ColoredEdges(G)
    new_graph = BreakGraph(graph, i1, i2, j1, j2)
    new_genome = GraphToGenome(new_graph)
    
    return new_genome
 
def NonTrivialCycle(G1, G2):
    '''Return any non-trivial cycle from Graph'''

    cycle = []
    redturn = True
    
    while (len(G1) > 0) or (len(G2) > 0):
        if cycle == []:
            if redturn:
                curr_edge = G1[0]
                G1.remove(curr_edge)
            else:
                curr_edge = G2[0]
                G2.remove(curr_edge)
            
            redturn = not redturn            
            
            new_edge = []
            curr_node = curr_edge[1] 
            cycle.append(curr_edge)
        
        if redturn:
            for edge in G1:
                if curr_node in edge:
                    cycle.append(edge)
                    new_edge = edge
                    G1.remove(edge)
                    break
        else:
            for edge in G2:
                if curr_node in edge:
                    cycle.append(edge)
                    new_edge = edge
                    G2.remove(edge)
                    break            
        
        if new_edge == []: #cycle is done
            if len(cycle) == 2:
                cycle = []
            else:
                return cycle
            
        else: #we found new edge in chain
            redturn = not redturn
            curr_edge = new_edge * 1
            new_edge = []
            if curr_node == curr_edge[0]:
                curr_node = curr_edge[1]
            else:
                curr_node = curr_edge[0]

        if len(cycle) > 4:
            return cycle
    
    if len(cycle) == 2:
        cycle = []
        
    return cycle    
    
def NonTrivialCycleGraph(G1, G2):
    '''Return any non-trivial cycle from Graph formed by
    dictionaries G1 and G2'''

    cycle = []
    redturn = True
    
    while (len(G1) > 0) or (len(G2) > 0):
        if cycle == []:
            if redturn:
                index = G1.keys()[0]
                curr_edge = [index, G1[index]]
                G1.pop(curr_edge[0])
                G1.pop(curr_edge[1])
            else:
                index = G2.keys()[0]
                curr_edge = [index, G2[index]]
                G2.pop(curr_edge[0])
                G2.pop(curr_edge[1])
            
            redturn = not redturn            
            
            curr_node = curr_edge[1] 
            cycle.append(curr_edge)
        
        if redturn:
            if curr_node in G1:
                curr_edge = [curr_node, G1[curr_node]]
                curr_node = curr_edge[1]
                cycle.append(curr_edge)
                G1.pop(curr_edge[0])
                G1.pop(curr_edge[1])
                redturn = not redturn
            else:
                if len(cycle) == 2:
                    cycle = []
                else:
                    return cycle                

        else:
            if curr_node in G2:
                curr_edge = [curr_node, G2[curr_node]]
                curr_node = curr_edge[1]
                cycle.append(curr_edge)
                G2.pop(curr_edge[0])
                G2.pop(curr_edge[1])
                redturn = not redturn
            else:
                if len(cycle) == 2:
                    cycle = []
                else:
                    return cycle                            

        if len(cycle) > 3:
            return cycle
    
    if len(cycle) == 2:
        cycle = []
        
    return cycle    
   
def CycleCount(G1, G2):
    '''Return count of cycles in graph united by G1 and G2'''

    cycle = []
    count = 0
    redturn = True
    
    while (len(G1) > 0) or (len(G2) > 0):
        if cycle == []:
            if redturn:
                curr_edge = G1[0]
                G1.remove(curr_edge)
            else:
                curr_edge = G2[0]
                G2.remove(curr_edge)
            
            redturn = not redturn            
            
            new_edge = []
            curr_node = curr_edge[1] 
            cycle.append(curr_edge)
        
        if redturn:
            for edge in G1:
                if curr_node in edge:
                    cycle.append(edge)
                    new_edge = edge
                    G1.remove(edge)
                    break
        else:
            for edge in G2:
                if curr_node in edge:
                    cycle.append(edge)
                    new_edge = edge
                    G2.remove(edge)
                    break            
                
        
        if new_edge == []: #cycle is done
            cycle = []
            count += 1
            
        else: #we found new edge in chain
            redturn = not redturn
            curr_edge = new_edge * 1
            new_edge = []
            if curr_node == curr_edge[0]:
                curr_node = curr_edge[1]
            else:
                curr_node = curr_edge[0]
        
    if cycle <> []:
        count += 1
        
    return count      
 
def ShortestRearrangementGraph(P, Q):
    '''Rearrange genome P with 2-breaks, in shortest way, to Q
    Both represented as set of synteny blocks'''
    reversals = [P]
    RedEdges = ColoredEdgesGraph(P)
    BlueEdges = ColoredEdgesGraph(Q)

    for i in range(10000):
        RedCopy = RedEdges.copy()
        BlueCopy = BlueEdges.copy()
    
        cycle = NonTrivialCycleGraph(RedCopy, BlueCopy)
   
    while cycle <> []:
        if (cycle[1][0] in BlueEdges) and (cycle[1][1] == BlueEdges[cycle[1][0]]):
            j1, i2 = cycle[1]
        else:
            return '2nd node is not blue!'
            
        i1 = cycle[0][0]
        RedEdges.pop(i1)
        RedEdges.pop(j1)
        
        j2 = cycle[2][1]
        RedEdges.pop(i2)
        RedEdges.pop(j2)
        
        RedEdges[j1] = i2
        RedEdges[i2] = j1
        RedEdges[j2] = i1
        RedEdges[i1] = j2
            
        RedCopy = RedEdges.copy()
        P = GraphToGenomeGraph(RedCopy)
        reversals.append(P)
        #print len(P)
        #print len(Q)
    
        RedCopy = RedEdges.copy()
        BlueCopy = BlueEdges.copy()        
        cycle = NonTrivialCycleGraph(RedCopy, BlueCopy)
    
    return reversals

   
def ShortestRearrangement(P, Q):
    '''Rearrange P with 2-breaks, in shortest way, to Q'''
    #reversals = [P]
    reversals = 0
    RedEdges = ColoredEdges(P)
    BlueEdges = ColoredEdges(Q)
    Graph = RedEdges + BlueEdges
    cycle = NonTrivialCycle(Graph)
    while cycle <> []:
        for i in range(1, len(cycle)):
            if cycle[i] in BlueEdges:
                break
        j1, i2 = cycle[i]
        
        '''if cycle[i-1][1] == j1:
            i1 = cycle[i-1][0]
        if cycle[i-1][0] == j1:
            i1 = cycle[i-1][1]
        RedEdges.remove(cycle[i-1])
        
        if cycle[i+1][1] == i2:
            j2 = cycle[i+1][0]
        if cycle[i+1][0] == i2:
            j2 = cycle[i+1][1]
        RedEdges.remove(cycle[i+1])'''
        
        for edge in (cycle[i-1], cycle[i+1]):
            if edge[1] == j1:
                i1 = edge[0]
                RedEdges.remove(edge)
                break
            if edge[0] == j1:
                i1 = edge[1]
                RedEdges.remove(edge)
                break

        for edge in (cycle[i-1], cycle[i+1]):
            if edge[1] == i2:
                j2 = edge[0]
                RedEdges.remove(edge)
                break
            if edge[0] == i2:
                j2 = edge[1]
                RedEdges.remove(edge)
                break
    
        #RedEdges = BreakGraph(RedEdges, i1, j1, j2, i2)
        RedEdges.append([j1, i2])
        RedEdges.append([j2, i1])
        
        #P = GraphToGenome(RedEdges)
        #reversals.append(P)
        reversals += 1
        
        Graph = RedEdges + BlueEdges
        cycle = NonTrivialCycle(Graph)
    
    return reversals
        
    