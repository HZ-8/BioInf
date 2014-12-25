def ReadTextPattern (filename):
    f = open(filename, 'r')
    #Read data for Manhattan task
    '''line = f.readline().strip()
    n, m = line.split()
    
    array = []
    for line in f:
        if line[0] == '-':
            array1 = array * 1
            array = []
        else:
            row = line.strip().split()
            row = map(int, row)
            array.append(row)
    return n, m, array1, array'''
    
    #Read for LSC
    '''v = f.readline().strip()
    w = f.readline().strip()'''
    
    #Read for DAG
    '''start_node = f.readline().strip()
    end_node = f.readline().strip()
    start_node, end_node = map(int, [start_node, end_node])
    
    graph = {}
    for line in f:
       out_node, direction = line.strip().split('->')
       in_node, weight = direction.split(':')
       out_node, in_node, weight = map(int, [out_node, in_node, weight])
       
       if out_node in graph:
           graph[out_node].append([in_node, weight])
       else:
           graph[out_node] = [[in_node, weight]]
    
     return start_node, end_node, graph'''
    
    #Read data for Global Alignment
    v = f.readline().strip()
    w = f.readline().strip()

    f.close()    
    
    return v, w

def ReadScoreMatrix (filename):
    f = open(filename, 'r')
    
    letters = f.readline().strip()
    letters= letters.split()
    
    graph = {}
    for line in f:
        el = {}
        row = line.strip().split()
        key = row[0]
        values = row[1:]
        values = map(int, values)
        
        for i in range (len(values)):
            el[letters[i]] = values[i]
        
        graph[key] = el

    f.close()    
    
    return graph