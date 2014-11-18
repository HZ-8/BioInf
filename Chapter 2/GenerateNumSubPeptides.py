import GetNumPeptideMass as gsm

def GenerateNumSubPeptides(Peptide):
    '''Given a numeric peptide, return its cyclic spectrum'''
    subpeptides = [0]
    
    for i in range(len(Peptide)):
        for j in range(len(Peptide) -1):
            subpept = Peptide[i: i+j+1]
            if i + j + 1 >= len(Peptide):
                subpept = subpept + Peptide[: i+j - len(Peptide) + 1]
            subpeptides.append(gsm.GetNumPeptideMass(subpept))
    subpeptides.append(gsm.GetNumPeptideMass(Peptide))
    return subpeptides