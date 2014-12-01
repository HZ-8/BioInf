def StringComposition(Text, k):
    result = []
    for i in range(len(Text)-k+1):
        result.append(Text[i:i+k])
    result.sort()
    
    return result