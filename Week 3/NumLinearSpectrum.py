import GenerateLinNumSubPeptides as gsp, GetSpectrumMass as gsm

def NumLinearSpectrum(numPeptide):
    '''numPeptide is an array of aa masses. Return a numeric spectrum - 
    a list of masses of each possible sub peptide'''
    spectr =[0]
    parts = gsp.GenerateLinNumSubPeptides(numPeptide)
    
    for part in parts:
        spectr.append(gsm.GetSpectrumMass(part))
    
    spectr.sort()
    
    return spectr