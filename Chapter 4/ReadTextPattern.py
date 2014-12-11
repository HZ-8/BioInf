def ReadTextPattern (filename):
    f = open(filename, 'r')

    '''k = f.readline().strip()
    Text = f.readline().strip()'''
    
    line = f.readline().strip()
    k, d = line.split()
    '''array = {}
    for line in f:
        line_el = line.strip().split()
        key = int(line_el[0])
        s_values = line_el[2].split(',')
        values = []
        for el in s_values:
           values.append(int(el))
        array[key] = values'''
    
    array = []
    for line in f:
        line_el = line.strip().split('|')
        array.append(line_el)
        
    '''profile = {}
    prof_row = f.readline().strip()
    profile['A'] = map(float, prof_row.split())
    
    prof_row = f.readline().strip()
    profile['C'] = map(float, prof_row.split())

    prof_row = f.readline().strip()
    profile['G'] = map(float, prof_row.split())

    prof_row = f.readline().strip()
    profile['T'] = map(float, prof_row.split()) '''
    f.close()    
    
    return k, d, array