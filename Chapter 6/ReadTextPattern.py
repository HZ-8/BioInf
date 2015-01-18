def ReadTextPattern (filename):
    f = open(filename, 'r')
    #Read data for Greedy Search
    '''line = f.readline().strip()
    values = line.split()
    
    array = []
    for el in values:
        if el[0] == '(':
            el = el[1:]
        if el[-1] == ')':
            el = el[:-1]
        array.append(int(el))'''
    #Read data for ShortestReversals
    line = f.readline().strip()
    values = line.split(')')
    array1 = []
    for chrom in values:
        chr_array = []
        if chrom == '':
            continue
        blocks = chrom.split()
        
        for el in blocks:
            if el[0] == '(':
                el = el[1:]
            chr_array.append(int(el))
        array1.append(chr_array)
        
    line = f.readline().strip()
    values = line.split(')')
    array2 = []
    for chrom in values:
        chr_array = []
        if chrom == '':
            continue
        blocks = chrom.split()
        
        for el in blocks:
            if el[0] == '(':
                el = el[1:]
            chr_array.append(int(el))
        array2.append(chr_array)
        
    f.close()    
    
    return array1, array2