def CountBreakpoints(P):
    '''In a permutation P find count of breakpoints'''
    
    maxperm = len(P)
    new_p = [0] + P + [maxperm+1]
    count = 0
    for i in range(1, maxperm+2):
        if new_p[i-1] <> (new_p[i]-1):
            count += 1
            
    return count
    