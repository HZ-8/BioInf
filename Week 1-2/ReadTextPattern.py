def ReadTextPattern (filename):
    ''' This procedure takes anme of a file, and returns 2 strings from it -
    Text to search in, and Pattern to be searched for '''
    f = open(filename, 'r')
    Text = f.readline()
    #k = f.readline()
    #dist = f.readline()   
    f.close()
    return Text.strip()
    #return Text.strip()