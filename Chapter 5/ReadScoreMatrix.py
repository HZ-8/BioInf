def ReadTextPattern (filename):
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