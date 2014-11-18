import NumLinearSpectrum as ls

def LinearScore(numPeptide, Spectrum):
    '''Check how many valid positions exist in Spectrum for a theoretical
    linear spectrum of numeric Peptide'''
    
    theor_spec = ls.NumLinearSpectrum(numPeptide)

    tsp2 = Spectrum + []
    count = 0

    for el in theor_spec:
        if el in tsp2:
            tsp2.remove(el)
            count +=1
            
    return count