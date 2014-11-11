#delete this file! GenerateNumSubPeptides generates cuclospectrum!!!

import GenerateNumSubPeptides as gsp, GetNumPeptideMass as gm

def NumCyclospectrum(numPeptide):
    '''numPeptide is an array of aa masses. Return a numeric spectrum - 
    a list of masses of each possible sub peptide'''
    spectr =[0]
    parts = gsp.GenerateNumSubPeptides(numPeptide)
    
    for part in parts:
        spectr.append(gm.GetNumPeptideMass(part))
    
    spectr.sort()
    
    return spectr