import PatternToNumber

def ComputingFrequencies(Text, k):
    ''' This procedure finds in Text frequency of each k-mer'''
    FrequencyArray = [0] * (4 ** k)
    for i in range(len(Text) - k + 1):
        Pattern =  Text[i: i + k]
        j = PatternToNumber.PatternToNumber(Pattern)
        FrequencyArray[j] += 1
    return FrequencyArray
    
    
