def LCSBackTrack(v1, v2, v3):
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

    Backtrack = []        
    for i in range (n+1):
        table = []
        for j in range(m+1):
            row = []
            for k in range(l+1):
                row.append([0, 0, 0])
            table.append(row)
        Backtrack.append(table)
        
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
                                from_node = [i1, i2,  i3]

                nodes[i][j][k] = max_score
                Backtrack[i][j][k] = from_node
    
    return nodes[n][m][l], Backtrack

def OutputLCS(Backtrack, v1, v2, v3, i, j):
    '''Solve the Longest Common Subsequence Problem by using the information
    in Backtrack. '''
    n = len(v1)
    m = len(v2)
    l = len(v3)
    p1 = '' #v1[len(v1)-1]
    p2 = '' #v2[len(v2)-1]
    p3 = '' #v3[len(v3)-1]
    
    path = [n-1, m-1, l-1]
    from_node = Backtrack[n-1][m-1][l-1]

    while from_node <> [0,0,0]:
        path = Backtrack[from_node] + path
        from_node = Backtrack[from_node]
    
    