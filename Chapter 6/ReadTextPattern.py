def ReadTextPattern (filename):
    f = open(filename, 'r')
    #Read data for Greedy Search
    line = f.readline().strip()
    values = line.split()
    
    array = []
    for el in values:
        if el[0] == '(':
            el = el[1:]
        if el[-1] == ')':
            el = el[:-1]
        array.append(int(el))

    f.close()    
    
    return array