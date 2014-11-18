import HammingDistance as HD

def ApproximatePatternMatching(Pattern, Text, dist):
    '''Finds in Text all Patterns and similar patterns of distance <-dist'''
    pos = []
    k = len(Pattern)
    for i in range(len(Text) - k + 1):
        if HD.HammingDistance(Text[i: i + k], Pattern) <= dist:
            pos.append(i)
    return pos