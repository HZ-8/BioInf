def LocalAlignment(v, w, Score, sigma):
    '''Find the maximum score of a local alignment of the strings, followed
    by a local alignment of these strings achieving the maximum score'''
    
    n = len(v)
    m = len(w)
    nodes = []
    for i in range (n+1):
        row = []
        for j in range(m+1):
            row.append(0)
            
        nodes.append(row)
    
    Backtrack = []        
    for i in range (n):
        backrow = []
        for j in range(m):
            backrow.append('')
        Backtrack.append(backrow)
    
    maxscore = 0
    sink_node = [0, 0]
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            vert_path = nodes[i-1][j] - sigma
            hor_path = nodes[i][j-1] - sigma
            diag_path = nodes[i-1][j-1] + Score[v[i-1]][w[j-1]]
            zero_path = 0
            
            nodes[i][j] = max(zero_path, vert_path, hor_path, diag_path)
            
            if nodes[i][j] > maxscore:
                maxscore = nodes[i][j]
                sink_node = [i,j]
            
            if nodes[i][j] == zero_path:
               Backtrack[i-1][j-1] = 'Z'
            if nodes[i][j] == vert_path:
               Backtrack[i-1][j-1] = 'V'
            if nodes[i][j] == hor_path:
               Backtrack[i-1][j-1] = 'R'   
            if nodes[i][j] == diag_path:
               Backtrack[i-1][j-1] = 'D'

    
    return maxscore, sink_node, Backtrack
    
def OutputAlignment(Backtrack, v, i, j, position):
    '''Return alignment of v and w'''
    if (i >= 0) and (j == -1):
        if position == 1:
            return v[:i+1]
        else:
            return '-' * (i+1)
    elif (i == -1) and (j >= 0):
        if position == 1:
            return '-' * (j+1)
        else:
            return v[:j+1]
    elif (i == -1) and (j == -1):
        return ''
    
    if Backtrack[i][j] == 'V':
        if position == 1:
            return OutputAlignment(Backtrack, v, i-1, j, position) + v[i]
        else:
            return OutputAlignment(Backtrack, v, i-1, j, position) + '-'
    elif Backtrack[i][j] == 'R':
        if position == 1:
            return OutputAlignment(Backtrack, v, i, j-1, position) + '-'
        else:
            return OutputAlignment(Backtrack, v, i, j-1, position) + v[j]
    elif Backtrack[i][j] == 'D':
        if position == 1:
            return OutputAlignment(Backtrack, v, i-1, j-1, position) + v[i]
        else:
            return OutputAlignment(Backtrack, v, i-1, j-1, position) + v[j]
    elif Backtrack[i][j] == 'Z':
        return ''