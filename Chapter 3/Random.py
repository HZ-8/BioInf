def Random(array):
    s = sum(array)
    for i in range(len(array)):
        array[i] = float(array[i])/ s
    
    return array