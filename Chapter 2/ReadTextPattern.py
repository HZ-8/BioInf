def ReadTextPattern (filename):
    ''' This procedure takes name of a file, and returns 2 strings from it -
    Text to search in, and Pattern to be searched for '''
    f = open(filename, 'r')
    Pattern= f.readline()
    #k = f.readline()
    #dist = f.readline() 
    f.close()
    Pattern.strip()
    array = Pattern.split()
    
    array = map(int, array)
    
    return array