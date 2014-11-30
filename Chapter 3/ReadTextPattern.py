def ReadTextPattern (filename):
    f = open(filename, 'r')

    Text = f.readline().strip()
    k, t, N = Text.split()
    dna = []
    for line in f:
        dna.append(line.strip())

    '''profile = {}
    prof_row = f.readline().strip()
    profile['A'] = map(float, prof_row.split())
    
    prof_row = f.readline().strip()
    profile['C'] = map(float, prof_row.split())

    prof_row = f.readline().strip()
    profile['G'] = map(float, prof_row.split())

    prof_row = f.readline().strip()
    profile['T'] = map(float, prof_row.split()) '''
    
    return k, t, N, dna