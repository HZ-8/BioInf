def InitBacktrack(n, m, l):
    Backtrack = []        
    for i in range (n+1):
        table = []
        for j in range(m+1):
            row = []
            for k in range(l+1):
                row.append([])
            table.append(row)
        Backtrack.append(table)
    
    Backtrack[0][0][0] = [-1, -1, -1]
    i = 0
    for j in range(1, m+1):
        Backtrack[i][j][0] = [i, j-1, 0]
    for k in range(1, l+1):
        Backtrack[i][0][k] = [i, 0, k-1]
    for j in range(1, m+1):
        for k in range(1, l+1):
            Backtrack[i][j][k] = [i, j-1, k-1]
            
    j = 0
    for i in range(1, n+1):
        Backtrack[i][j][0] = [i-1, j, 0]
    for k in range(1, l+1):
        Backtrack[0][j][k] = [0, j, k-1]
    for i in range(1, n+1):
        for k in range(1, l+1):
            Backtrack[i][j][k] = [i-1, j, k-1]

    k = 0
    for i in range(1, n+1):
        Backtrack[i][0][k] = [i-1, 0, k]
    for j in range(1, m+1):
        Backtrack[0][j][k] = [0, j-1, k]
    for i in range(1, n+1):
        for j in range(1, m+1):
            Backtrack[i][j][k] = [i-1, j-1, k]
    
    return Backtrack

def MultipleAlignment(v1, v2, v3):
    '''For 3 strings, reconstruct its alignment graph and 
    find the graph to move from the end to start edge'''
    n = len(v1)
    m = len(v2)
    l = len(v3)
    nodes = []
    for i in range (n+1):
        table = []
        for j in range(m+1):
            row = []
            for k in range(l+1):
                row.append(0)
            table.append(row)
        nodes.append(table)

    Backtrack = InitBacktrack(n, m, l)
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                max_score = 0
                from_node = [i-1, j-1, k-1]
                for i1 in range(i-1, i+1):
                    for i2 in range(j-1, j+1):
                        for i3 in range(k-1, k+1):
                            if (i1 == i) and (i2 == j) and (i3 == k):
                                continue
                            score = nodes[i1][i2][i3]
                            if (i1 == i-1) and (i2 == j-1) and (i3 == k-1):
                                if v1[i1] == v2[i2] == v3[i3]:
                                    score +=1
                            if score > max_score:
                                max_score = score * 1
                                from_node = [i1, i2, i3]

                nodes[i][j][k] = max_score
                Backtrack[i][j][k] = from_node
    
    return nodes[n][m][l], Backtrack

def OutputLCS(Backtrack, v1, v2, v3):
    '''Solve the Longest Common Subsequence Problem by using the information
    in Backtrack. '''
    n = len(v1)
    m = len(v2)
    l = len(v3)

    path = [[n, m, l]]
    print 'path', path
    from_node = Backtrack[n][m][l]
    print 'from node', from_node

    while from_node <> [0, 0, 0]:
        path = [from_node] + path
        print 'path', path
        from_node = Backtrack[from_node[0]][from_node[1]][from_node[2]]
        print 'from node', from_node
    path = [from_node] + path    
    
    '''start_node = path[0]
    p1 = '-' * start_node[0]
    p2 = '-' * start_node[1]
    p3 = '-' * start_node[2]'''
    
    return path
        
    