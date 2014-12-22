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
    v = f.readline().strip()
    w = f.readline().strip()

    f.close()    
    
    return v, w