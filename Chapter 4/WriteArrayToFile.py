def WriteArrayToFile (array, filename = 'result.txt'):
    ''' This procedure takes a name of a file and writes to it an array of data'''
    f = open(filename, 'w')
    #array = map(str, array)
    '''s = ' '.join(array)
    f.write(s)'''
    for el in array:
        f.write(el[0] + ' -> ' + el[1])
        f.write('\n')

    f.close()
    
    return