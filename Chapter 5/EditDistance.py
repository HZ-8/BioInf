def EditAlignment(v, w, sigma = 1):
    '''Find maximum alignment score of the strings v and w,
    and an alignment achieving this maximum score.
    Use the Score scoring matrix and indel penalty sigma'''
    
    n = len(v)
    m = len(w)
    nodes = []
    for i in range (n+1):
        row = []
        for j in range(m+1):
            row.append(0)
            
        nodes.append(row)
    
    for i in range (n):
        nodes[i+1][0] = nodes[i][0] - sigma
    for j in range (m):
        nodes[0][j+1] = nodes[0][j] - sigma   
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            vert_path = nodes[i-1][j] - sigma
            hor_path = nodes[i][j-1] - sigma
            diag_path = nodes[i-1][j-1]
            if [v[i-1]] <> [w[j-1]]:
                diag_path -= 1
            nodes[i][j] = max(vert_path, hor_path, diag_path)
            
    return nodes[n][m]