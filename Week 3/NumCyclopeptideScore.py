import GenerateNumSubPeptides as sp

def NumCyclopeptideScore(numPeptide, Spectrum):
    '''Check how many valid positions in Spectrum for a num Peptide'''    
    theor_spec = sp.GenerateNumSubPeptides(numPeptide)
    
    tsp1 = theor_spec + []
    tsp2 = Spectrum + []
    
    count = 0

    for el in tsp1:
        if el in tsp2:
            tsp2.remove(el)
            count +=1
    
    return count