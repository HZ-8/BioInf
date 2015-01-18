def WriteArrayToFile (array, filename = 'result.txt'):
    ''' This procedure takes a name of a file and writes to it an array of data'''
    f = open(filename, 'w')
    
    '''for revstep in array:
        strarray = []
        for pos in revstep:
            sign = ''
            if pos > 0:
                sign = '+'
            strarray.append(sign + str(pos))
            
        s = ' '.join(strarray)
        f.write('(' + s + ')')
        f.write('\n')'''
        
    for pair in array:
        p1 = str(pair[0])
        p2 = str(pair[1])
        
        f.write('(' + p1 + ', ' + p2 + ')')
        f.write('\n')     
        
    f.close()
    
    return