import GetSpectrumMass as gsm

def GenerateNumSubPeptides(Peptide):
    subpeptides = [0]
    
    for i in range(len(Peptide)):
        for j in range(len(Peptide) -1):
            subpept = Peptide[i: i+j+1]
            if i + j + 1 >= len(Peptide):
                subpept = subpept + Peptide[: i+j - len(Peptide) + 1]
            subpeptides.append(gsm.GetSpectrumMass(subpept))
    subpeptides.append(gsm.GetSpectrumMass(Peptide))
    return subpeptides