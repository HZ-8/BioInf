def HalfPath(v, w, Score, sigma):
    '''For v, w find scores for each node from start node
    Store only 2 columns'''
    n = len(v)
    m = len(w)
    path = []
    for i in range (n+1):
        row = []
        for j in range(2):
            row.append(0)
            
        path.append(row)
    
    for i in range (n):
        path[i+1][1] = path[i][1] - sigma   
    
    for j in range(1, m+1):    
        for i in range(n+1):
            path[i][0] = path[i][1] * 1
            if i == 0:
                path[i][1] = path[i][0] - sigma
            else:
                vert_path = path[i-1][1] - sigma
                hor_path = path[i][0] - sigma
                diag_path = path[i-1][0] + Score[v[i-1]][w[j-1]]
                path[i][1] = max(vert_path, hor_path, diag_path)
    return path

def MiddleEdge(v, w, Score, sigma):
    n = len(v)
    m = len(w)
    m_mid = m / 2
    
    w1 = w[:m_mid]
    from_s = HalfPath(v, w1, Score, sigma)
    v_rev = v[::-1]
    w_rev = w[m_mid:][::-1]
    to_s = HalfPath(v_rev, w_rev, Score, sigma)    
    mid_scores = []
    for i in range(n+1):
        mid_scores.append(from_s[i][1] + to_s[n-i][1])
        
    edge_start = (0, m_mid)
    max_path = mid_scores[0]
    for i in range(1, n+1):
        if mid_scores[i] > max_path:
            max_path = mid_scores[i]
            edge_start = (i, m_mid)
    
    i = edge_start[0]
    if i == n:
        edge_end = (edge_start[0], edge_start[1] + 1)
    else:
        hor_path = to_s[n-i][0] - sigma
        vert_path = to_s[n-i-1][1]- sigma
        diag_path = to_s[n-i-1][0] + Score[v[i]][w[m_mid]]
        
        max_score = max(hor_path, vert_path, diag_path)
        if max_score == hor_path:
            edge_end = (edge_start[0], edge_start[1] + 1)
        if max_score == vert_path:
            edge_end = (edge_start[0] + 1, edge_start[1])
        if max_score == diag_path:
            edge_end = (edge_start[0] + 1, edge_start[1] + 1)            
    
    return edge_start, edge_end

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
        
    edge_start, edge_end = MiddleEdge(v, w, Score, sigma)
    
    
    if edge_start[1] == edge_end[1]:
       direction = 'V'
    elif edge_start[0] == edge_end[0]:
       direction = 'R'
    else:
       direction = 'D'
    
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
        if d == 'R':
            path1 += '-'
            path2 += w[j]
            j+=1
        
    return path1, path2