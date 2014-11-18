def ReadTextPattern (filename):
    f = open(filename, 'r')
    Text = f.readline()
    Text = Text.strip()
    (k, d) = Text.split()
    dna = []
    for line in f:
        dna.append(line.strip())
    #k = f.readline()
    #dist = f.readline()   
    f.close()
    return k, d, dna
    #return Text.strip()