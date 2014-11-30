from random import random

def Random(array):
    s = sum(array)
    for i in range(len(array)):
        array[i] = float(array[i])/ s
    return array

def ProfileMostProbableKMer(Text, k, profile):
    max_probab = 0
    best_pat = Text[:k]
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        pat_probab = 1
        for j in range(k):
            pat_probab = pat_probab * profile[pattern[j]][j]
        if pat_probab > max_probab:
            max_probab = pat_probab
            best_pat = pattern
    
    return best_pat
    
def ProfileRandomlyGeneratedKMer(Text, k, profile):
    probab_array = []
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        pat_probab = 1
        for j in range(k):
            pat_probab = pat_probab * profile[pattern[j]][j]
        probab_array.append(pat_probab)
    
    probab_array = Random(probab_array)
    ran_number = random()
    prob_sum = probab_array[0]
    i = 0
    while prob_sum < ran_number:
        i += 1
        prob_sum += probab_array[i]
    
    return Text[i:i+k] 