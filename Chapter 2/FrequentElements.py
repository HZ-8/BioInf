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
    freq = sorted(freq.items(), key=lambda x: x[1], reverse = True)

    exper_masses = []

    for i in range(M):
        exper_masses.append(freq[i][0])
        
    i = M
    while (i < len(freq)) and (freq[i][1] == freq[i-1][1]):
        exper_masses.append(freq[i][0])
        i += 1

    return exper_masses