def AffineAlignment(v, w, Score, sigma, eps):
    
    n = len(v)
    m = len(w)
    mid_nodes = []
    low_nodes = []
    up_nodes = []
    for i in range (n+1):
        row = []
        for j in range(m+1):
            row.append(0)
            
        mid_nodes.append(row + [])
        low_nodes.append(row + [])
        up_nodes.append(row + [])
        
    up_nodes[0][1] = -sigma
    for j in range(2, m+1):
        up_nodes[0][j] = up_nodes[0][j-1] - eps
        
    low_nodes[1][0] = -sigma
    for i in range(2, n+1):
        low_nodes[i][0] = low_nodes[i-1][0] - eps

    Backtrack = []        
    for i in range (n):
        backrow = []
        for j in range(m):
            backrow.append('')
        Backtrack.append(backrow)
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            low_path1 = low_nodes[i-1][j] - eps
            low_path2 = mid_nodes[i-1][j] - sigma            
            low_nodes[i][j] = max(low_path1, low_path2)
               
            up_path1 = up_nodes[i][j-1] - eps
            up_path2 = mid_nodes[i][j-1] - sigma            
            up_nodes[i][j] = max(up_path1, up_path2)      
            
            mid_path1 = low_nodes[i][j]
            mid_path2 = mid_nodes[i-1][j-1] + Score[v[i-1]][w[j-1]]            
            mid_path3 = up_nodes[i][j]          
            mid_nodes[i][j] = max(mid_path1, mid_path2, mid_path3)
             
            if mid_nodes[i][j] == mid_path1:
               Backtrack[i-1][j-1] = 'V'
            elif mid_nodes[i][j] == mid_path3:
               Backtrack[i-1][j-1] = 'R'
            else:
               Backtrack[i-1][j-1] = 'D'

    return mid_nodes[n][m], Backtrack
    
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
    else:
        if position == 1:
            return OutputAlignment(Backtrack, v, i-1, j-1, position) + v[i]
        else:
            return OutputAlignment(Backtrack, v, i-1, j-1, position) + v[j]