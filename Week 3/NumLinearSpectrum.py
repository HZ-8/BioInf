def NumLinearSpectrum(numPeptide):
    '''Take a letter peptide and return its linear spectrum, sorted'''
    
    PrefixMass = [0]
    for i in range(len(numPeptide)):
        PrefixMass.append(PrefixMass[i] + numPeptide[i])
    
    LinearSpectrum = [0]
    for i in range(len(numPeptide)):
        for j in range(i + 1, len(numPeptide) + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
   
    LinearSpectrum.sort()
    
    return LinearSpectrum