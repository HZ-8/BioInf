def NumCyclicSpectrum(numPeptide):
    '''Take a numeric peptide and return its cyclic spectrum, sorted'''
        
    PrefixMass = [0]
    for i in range(len(numPeptide)):
        PrefixMass.append(PrefixMass[i] + numPeptide[i])
    
    PeptideMass = PrefixMass[len(PrefixMass) - 1]
    
    CyclicSpectrum = [0]
    for i in range(len(numPeptide)):
        for j in range(i + 1, len(numPeptide) + 1):
            CyclicSpectrum.append(PrefixMass[j] - PrefixMass[i])
            if (i > 0) and (j < len(numPeptide)):
                CyclicSpectrum.append(PeptideMass - PrefixMass[j] + PrefixMass[i])
   
    CyclicSpectrum.sort()
    
    return CyclicSpectrum