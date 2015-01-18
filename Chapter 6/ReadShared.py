def ReadTextPattern (filename):
    f = open(filename, 'r')

    k = f.readline().strip()
    G1 = f.readline().strip()
    G2 = f.readline().strip()
        
    f.close()    
    
    return k, G1, G2