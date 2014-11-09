import GetSpectrumMass as gsm

def GenerateLinNumSubPeptides(Peptide):
    '''Given a numeric peptide, return a list of its subpeptides,
    BUT WITHOUT cyclic'''
    subpeptides = [0]
    
    for i in range(len(Peptide)):
        for j in range(len(Peptide) -1):
            if i + j + 1 <= len(Peptide):
                subpept = Peptide[i: i+j+1]
                subpeptides.append(gsm.GetSpectrumMass(subpept))
    subpeptides.append(gsm.GetSpectrumMass(Peptide))
    return subpeptides