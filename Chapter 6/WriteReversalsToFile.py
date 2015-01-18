def WriteReversalsToFile (Reversals, filename = 'result.txt'):
    ''' This procedure takes a name of a file and writes to it an array of data'''
    f = open(filename, 'w')
    
    for array in Reversals:
        for revstep in array:
            strarray = []
            for pos in revstep:
                sign = ''
                if pos > 0:
                    sign = '+'
                strarray.append(sign + str(pos))
                
            s = ' '.join(strarray)
            f.write('(' + s + ')')
        f.write('\n')
        
    f.close()
    
    return