import PatternCount

def FrequentWords(Text, k):
    ''' The procedure takes a string Text and an integer k, and returns
    all most frequent k-mers in Text'''
    FrequentPatterns = set()
    Count = [0] * (len(Text) - k + 1)
    for i in range (len(Text) - k):
        Pattern = Text[i: i + k]
        Count[i] = PatternCount.PatternCount(Text, Pattern)        
    maxCount = max(Count)
    for i in range(len(Text) - k):
        if Count[i] == maxCount:
            FrequentPatterns.add(Text[i: i + k])
    return FrequentPatterns