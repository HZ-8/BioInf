def ProfileMostProbableKMer(Text, k, profile):
    max_probab = 0
    best_pat = ''
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        pat_probab = 1
        for j in range(k):
            pat_probab = pat_probab * profile[pattern[j]][j]
        if pat_probab > max_probab:
            max_probab = pat_probab
            best_pat = pattern
    
    return best_pat