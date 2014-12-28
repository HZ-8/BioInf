def HalfPath(v, w, Score, sigma):
    n = len(v)
    m = len(w)
    path = []
    for i in range (n+1):
        row = []
        for j in range(m+1):
            row.append(0)
            
        path.append(row)
    
    for i in range (n):
        path[i+1][0] = path[i][0] - sigma
    for j in range (m):
        path[0][j+1] = path[0][j] - sigma   
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            vert_path = path[i-1][j] - sigma
            hor_path = path[i][j-1] - sigma
            diag_path = path[i-1][j-1] + Score[v[i-1]][w[j-1]]
            path[i][j] = max(vert_path, hor_path, diag_path)
    return path

def MiddleEdge(v, w, Score, sigma):
    n = len(v)
    m = len(w)
    m_mid = m / 2
    w1 = w[:m_mid+1]
    from_s = HalfPath(v, w1, Score, sigma)
    
    v_rev = v[::-1]
    w_rev = w[m_mid+1:][::-1]
    to_s = HalfPath(v_rev, w_rev, Score, sigma)    
    
    mid_score = []
    for i in range(n+1):
        mid_score.append(from_s[i][m_mid] + to_s[n+1-i][m-m_mid])
        
    edge_start = (0, m_mid)
    max_path = mid_score[0][m_mid]
    for i in range(1, n+1):
        if mid_score[i][m_mid] > max_path:
            max_path = mid_score[i][m_mid]
            edge_start = (i, m_mid)
    
    hor_path = - sigma
    diag_path = Score[v[edge_start[0]]][w[edge_start[1]]]
    if hor_path > diag_path:
        edge_end = (edge_start[0], edge_start[1] + 1)
    else:
        edge_end = (edge_start[0] + 1, edge_start[1] + 1)
    
    return max_path, edge_start, edge_end

def LinearSpaceAlignment(v, w, Score, sigma):
    
    if w == '':
        if v <> '':
            res = ['V'] * len(v)
        else:
            res = []
        return res
    if v == '':
        if w <> '':
            res = ['R'] * len(w)
        else:
            res = []
        return res
        
    max_path, edge_start, edge_end = MiddleEdge(v, w, Score, sigma)
    
    print edge_start
    print edge_end
    print max_path
    
    if edge_start[0] == edge_end[0]:
       direction = 'V'
    elif edge_start[1] == edge_end[1]:
       direction = 'R'
    else:
       direction = 'D'
    print direction
    
    v1 = v[:edge_start[0]]
    v2 = v[edge_end[0]:]
    
    w1 = w[:edge_start[1]]
    w2 = w[edge_end[1]:]
    res = LinearSpaceAlignment(v1, w1, Score, sigma) + \
                               [direction] + \
                LinearSpaceAlignment(v2, w2, Score, sigma)                                 
    return res  

def GetPath(v, w, directions):
    path1 = ''
    path2 = ''
    i = 0
    j = 0
    for d in directions:
        if d == 'D':
            path1 += v[i]
            i+=1
            path2 += w[j]
            j += 1
        if d == 'V':
            path1 += v[i]
            i+=1
            path2 += '-'
        if d == 'H':
            path1 += '-'
            path2 += w[j]
            j+=1
        
    return path1, path2