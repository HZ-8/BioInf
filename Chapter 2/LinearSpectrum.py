def LinearSpectrum(Peptide, AminoAcidDict):
    '''Take a letter peptide and return its linear spectrum, sorted'''
    
    PrefixMass = [0]
    for i in range(len(Peptide)):
        PrefixMass.append(PrefixMass[i] + AminoAcidDict[Peptide[i]])
    
    LinearSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
   
    LinearSpectrum.sort()
    
    return LinearSpectrum