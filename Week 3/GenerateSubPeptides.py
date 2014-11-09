def GenerateSubPeptides(Peptide):
    subpeptides = []
    
    for i in range(len(Peptide)):
        for j in range(len(Peptide) -1):
            subpept = Peptide[i: i+j+1]
            if i + j + 1 >= len(Peptide):
                subpept = subpept + Peptide[: i+j - len(Peptide) + 1]
            subpeptides.append(subpept)
    subpeptides.append(Peptide)
    return subpeptides
        