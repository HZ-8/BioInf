import GetSpectrumMass as gsm

def GenerateLinNumSubPeptides(numPeptide):
    '''Given a numeric peptide, return a list of its subpeptides,
    BUT WITHOUT cyclic'''
    subpeptides = [0]
    
    for i in range(len(numPeptide)):
        for j in range(len(numPeptide) -1):
            if i + j + 1 <= len(numPeptide):
                subpept = numPeptide[i: i+j+1]
                subpeptides.append(gsm.GetSpectrumMass(subpept))
    subpeptides.append(gsm.GetSpectrumMass(numPeptide))
    return subpeptides