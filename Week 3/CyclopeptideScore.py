import GenerateTheoreticalSpectrum as gts, CyclicSpectrum as cs

def CyclopeptideScore(Peptide, Spectrum, aamass):
    '''Check how many valid positions in Spectrum for a Peptide'''    
    theor_spec = gts.GenerateTheoreticalSpectrum(Peptide, aamass)
    
    tsp1 = theor_spec + []
    tsp2 = Spectrum + []
    
    count = 0

    for el in tsp1:
        if el in tsp2:
            tsp2.remove(el)
            count +=1
    
    return count

def NumCyclopeptideScore(numPeptide, Spectrum):
    '''Check how many valid positions in Spectrum for a num Peptide'''    
    theor_spec = cs.NumCyclicSpectrum(numPeptide)
    
    tsp2 = Spectrum + []
    
    count = 0

    for el in theor_spec:
        if el in tsp2:
            tsp2.remove(el)
            count +=1
    
    return count