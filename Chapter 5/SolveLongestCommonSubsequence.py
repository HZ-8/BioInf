def LCSBackTrack(v, w):
    '''For 2 strings, reconstruct its alignment graph and 
    find the graph to move from the end to start edge'''
    n = len(v)
    m = len(w)
    nodes = []
    Backtrack = []
    for i in range (n+1):
        row = []
        backrow = []
        for j in range(m+1):
            row.append(0)
            backrow.append('none')
        nodes.append(row)
        Backtrack.append(backrow)
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            vert_path = nodes[i-1][j]
            hor_path = nodes[i][j-1]
            diag_path = nodes[i-1][j-1]
            if v[i-1] == w[j-1]:
                diag_path += 1
            nodes[i][j] = max(vert_path, hor_path, diag_path)
            
            if nodes[i][j] == nodes[i-1][j]:
               Backtrack[i][j] = 'Vert'
            if nodes[i][j] == nodes[i][j-1]:
               Backtrack[i][j] = 'Right'   
            if (nodes[i][j] == nodes[i-1][j-1] + 1) and (v[i-1] == w[j-1]):
               Backtrack[i][j] = 'Diag'      
    
    return Backtrack

def OutputLCS(Backtrack, v, i, j):
    '''Solve the Longest Common Subsequence Problem by using the information
    in Backtrack. OUTPUTLCS(Backtrack, v, i, j) outputs an LCS between the
    i-prefix of v and the j-prefix of w '''
    if (i == 0) or (j == 0):
        return ''
    
    if Backtrack[i][j] == 'Vert':
        return OutputLCS(Backtrack, v, i-1, j) + v[i]      
    elif Backtrack[i][j] == 'Right':
        return OutputLCS(Backtrack, v, i, j-1) + v[i]
    else:
        return OutputLCS(Backtrack, v, i-1, j-1) + v[i]