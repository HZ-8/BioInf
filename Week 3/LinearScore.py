import GenerateLinTheoreticalSpectrum as gts

def LinearScore(numPeptide, Spectrum):
    '''Check how many valid positions exist in Spectrum for a theoretical
    linear spectrum of numeric Peptide'''
    theor_spec = gts.GenerateLinTheoreticalSpectrum(numPeptide)
    tsp1 = theor_spec + []
    tsp2 = Spectrum + []

    count = 0

    for el in tsp1:
        if el in tsp2:
            tsp2.remove(el)
            count +=1
            
    return count