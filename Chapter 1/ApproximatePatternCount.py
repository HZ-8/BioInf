import HammingDistance as HD

def ApproximatePatternCount(Text, Pattern, dist):
    '''Finds in Text all Patterns and similar patterns of distance <-dist'''
    count = 0
    k = len(Pattern)
    for i in range(len(Text) - k + 1):
        if HD.HammingDistance(Text[i: i + k], Pattern) <= dist:
            count +=1
    return count