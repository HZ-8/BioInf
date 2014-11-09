import GenerateNumSubPeptides as gsp, GetSpectrumMass as gsm

def NumCyclospectrum(numPeptide):
    '''numPeptide is an array of aa masses. Return all possible sub peptides
    as list of numeris lists'''
    spectr =[0]
    parts = gsp.GenerateNumSubPeptides(numPeptide)
    
    for part in parts:
        spectr.append(gsm.GetSpectrumMass(part))
    
    spectr.sort()
    
    return spectr