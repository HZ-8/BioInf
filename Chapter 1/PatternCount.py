def PatternCount(Text, Pattern):
    ''' This procedure takes Text and Pattern, and returns count of times
    that Pattern appears in Text'''
    count = 0
    for i in range (len(Text) - len(Pattern) + 1):
        if Text[i: i + len(Pattern)] == Pattern:
            count += 1
    return count