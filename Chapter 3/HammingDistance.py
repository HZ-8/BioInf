def HammingDistance(p, q):
    dist = 0
    for i in range (len(p)):
        if p[i] != q[i]:
            dist +=1
    return dist