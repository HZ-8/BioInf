def WriteArrayToFile (array, filename = 'result.txt'):
    ''' This procedure takes a name of a file and writes to it an array of data'''
    f = open(filename, 'w')
    array = map(str, array)
    s = '->'.join(array)
    f.write(s)
    '''array.sort()
    for path in array:
        f.write(path[0])
        for i in range(1, len(path)):
            f.write(path[i][-1])
        f.write('\n')'''

    f.close()
    
    return