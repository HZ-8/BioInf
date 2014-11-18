def WriteArrayToFile (array, filename = 'result.txt'):
    ''' This procedure takes a name of a file and writes to it an array of data'''
    f = open(filename, 'w')
    for i in range(len(array)):
        f.write(str(array[i]))
        f.write(', ')
    f.close()