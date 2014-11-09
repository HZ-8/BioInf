def SpectrumMatch(spec1, spec2):
    '''Find spec1 in spec2'''
    tsp1 = spec1 + []
    tsp2 = spec2 + []

    for el in tsp1:
        if el in tsp2:
            tsp2.remove(el)
        else: return False
    
    return True