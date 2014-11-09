import PatternToNumber as pn, NumberToPattern as np

def FindingFrequentWordsBySorting(Text, k):
    FrequentPatterns = set()
    Index = []
    Count = [1] * (len(Text) - k + 1)
    for i in range(len(Text) - k + 1):
        Pattern = Text[i: i + k]
        Index.append(pn.PatternToNumber(Pattern))

    Index.sort()
    for i in range(len(Index) - 1):
        if Index[i + 1] == Index[i]:
            Count[i + 1] = Count[i] + 1
       
    maxCount = max(Count)
    for i in range(len(Count)):
        if Count[i] == maxCount:
            Pattern = np.NumberToPattern(Index[i], k)
            FrequentPatterns.add(Pattern)
    
    return FrequentPatterns