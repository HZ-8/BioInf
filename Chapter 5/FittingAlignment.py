def FittingAlignment(v, w, sigma):
    
    n = len(v)
    m = len(w)
    nodes = []
    for i in range (n+1):
        row = []
        for j in range(m+1):
            row.append(0)
            
        nodes.append(row)
    
    for j in range (m):
        nodes[0][j+1] = nodes[0][j] - sigma   
    
    Backtrack = []        
    for i in range (n):
        backrow = []
        for j in range(m):
            backrow.append('')
        Backtrack.append(backrow)  
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            vert_path = nodes[i-1][j] - sigma
            hor_path = nodes[i][j-1] - sigma
            diag_path = nodes[i-1][j-1]
            if v[i-1] == w[j-1]:
                diag_path += 1
            else:
                diag_path -= 1
            
            nodes[i][j] = max(vert_path, hor_path, diag_path)
            
            if nodes[i][j] == vert_path:
               Backtrack[i-1][j-1] = 'V'
            if nodes[i][j] == hor_path:
               Backtrack[i-1][j-1] = 'R'   
            if nodes[i][j] == diag_path:
               Backtrack[i-1][j-1] = 'D'
    
    max_score = nodes[0][m]
    sink = [0, m]
    for i in range (1, n+1):
        if nodes [i][m] > max_score:
            max_score = nodes [i][m]
            sink = [i, m]
    
    return max_score, sink, Backtrack
    
def FittingPath(Backtrack, v, i, j, position):
    '''Return fitting alignment of v and w'''
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
            return FittingPath(Backtrack, v, i-1, j, position) + v[i]
        else:
            return FittingPath(Backtrack, v, i-1, j, position) + '-'
    elif Backtrack[i][j] == 'R':
        if position == 1:
            return FittingPath(Backtrack, v, i, j-1, position) + '-'
        else:
            return FittingPath(Backtrack, v, i, j-1, position) + v[j]
    elif Backtrack[i][j] == 'D':
        if position == 1:
            return FittingPath(Backtrack, v, i-1, j-1, position) + v[i]
        else:
            return FittingPath(Backtrack, v, i-1, j-1, position) + v[j]