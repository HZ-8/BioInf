def ManhattenTourist(n, m, Down, Right):
    '''In n+1 x m+1 matrix, find the longest path from 00 to nm node
    Down is a matrix of vertical edge weights of size n x (m+1)
    Right is a matrix of horizontal edge weights, of size (n+1) x m '''
    
    nodes = []
    for i in range (n+1):
        row = []
        for j in range(m+1):
            row.append(0)
        nodes.append(row)
    
    for i in range(1, n+1):
        nodes[i][0] = nodes[i-1][0] + Down[i-1][0]
    for j in range(1, m+1):
        nodes[0][j] = nodes[0][j-1] + Right[0][j-1]    

    for j in range(1, m+1):
        for i in range(1, n+1):
            vert_path = nodes[i-1][j] + Down[i-1][j]
            hor_path = nodes[i][j-1] + Right[i][j-1]
            nodes[i][j] = max(vert_path, hor_path)
    
    return nodes[n][m]
    
def DiagonalManhattenTourist(n, m, Down, Right, Diagonal):
    '''In n+1 x m+1 matrix, find the longest path from 00 to nm node
    Down is a matrix of vertical edge weights of size n x (m+1)
    Right is a matrix of horizontal edge weights, of size (n+1) x m
    Diagonal is a set of diagonal edges'''
    
    nodes = []
    for i in range (n+1):
        row = []
        for j in range(m+1):
            row.append(0)
        nodes.append(row)
    
    for i in range(1, n+1):
        nodes[i][0] = nodes[i-1][0] + Down[i-1][0]
    for j in range(1, m+1):
        nodes[0][j] = nodes[0][j-1] + Right[0][j-1]    

    for j in range(1, m+1):
        for i in range(1, n+1):
            vert_path = nodes[i-1][j] + Down[i-1][j]
            hor_path = nodes[i][j-1] + Right[i][j-1]
            diag_path = nodes[i-1][j-1] + Diagonal[i-1][j-1]
            nodes[i][j] = max(vert_path, hor_path, diag_path)
    
    return nodes[n][m]