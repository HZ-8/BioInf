import Neighbors as nb, PatternToNumber as pn, NumberToPattern as np, \
       ReverseComplementPattern as rev

def FrequentWordsWMismatchAndCompl(Text, k , d):
    '''In Text, find most frequent k-mers with up to d mismatches'''
    FrequentPatterns = set() #list of most freq patterns
    
    Patterns = [] #a list of k-mers in Text along with their d-modifications
    for i in range (len(Text) - k + 1):
        neighbors1 = nb.Neighbors(Text[i: i + k], d)
        compl = rev.ReverseComplementPattern(Text[i: i + k])
        neighbors2 = nb.Neighbors(compl, d)
        Patterns = Patterns + neighbors1 + neighbors2
    
    #for each Pattern, find its frequency in Text;
    #transform formPatterns to list type
    #form Index which is a list of Pattern numbers, and sort it
    Index = []
    for i in range (len(Patterns)):
        Pattern = Patterns[i]
        Index.append(pn.PatternToNumber(Pattern))
    
    Count = [1] * len(Patterns)
    Index.sort()
    
    #find count of each Pattern
    for i in range(len(Index) - 1):
        if Index[i + 1] == Index[i]:
            Count[i + 1] = Count[i] + 1

    #Form a lsit of most frequent patterns       
    maxCount = max(Count)
    for i in range(len(Count)):
        if Count[i] == maxCount:
            Pattern = np.NumberToPattern(Index[i], k)
            FrequentPatterns.add(Pattern)
            
    return FrequentPatterns