def ReadTextPattern (filename):
    f = open(filename, 'r')
    Text = f.readline()
    Text = Text.strip()
    k = f.readline()
    k = k.strip()
    
    profile = {}
    prof_row = f.readline().strip()
    profile['A'] = map(float, prof_row.split())
    
    prof_row = f.readline().strip()
    profile['C'] = map(float, prof_row.split())

    prof_row = f.readline().strip()
    profile['G'] = map(float, prof_row.split())

    prof_row = f.readline().strip()
    profile['T'] = map(float, prof_row.split()) 
    
    return Text, k, profile
    #return Text.strip()