def Frequencies(Array):
    '''Take an array of elements; return a dictionary where each element
    is a key, its frequency - a value'''
    Array.sort()
    Frequencies = {}
    Count = [1] * (len(Array))
    
    Frequencies[Array[0]] = 1
    for i in range(len(Array) - 1):
        if Array[i + 1] == Array[i]:
            Count[i + 1] = Count[i] + 1
            Frequencies[Array[i+1]] = Count[i+1]
    
    return Frequencies
    
def FrequentElement(Array, M):
    '''Return M most frequest elements of array, with ties'''
    
    freq = Frequencies(Array)
    freq = sorted(freq.items(), reverse = True)
    
    exper_masses = []
    count = 0
    prev_elem = ''
    for elem_pair in freq:
        if count >= M:
            break
    
        exper_masses.append(elem_pair[0])
        if elem_pair[0] == prev_elem:
            prev_elem = elem_pair[0]
        else: 
            count += 1           

    return exper_masses