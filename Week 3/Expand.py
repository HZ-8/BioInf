def Expand(numPeptides, AminoMassesList):
    '''Take a list of numeric peptides, and return expanded list (added one 
    mass from list to the end of each peptide)'''
    exp_peptides = []
    
    if numPeptides == [0]:
        for mass in AminoMassesList:
            exp_peptides.append(mass)
        return exp_peptides
    
    for pept in numPeptides:
        for mass in AminoMassesList:
            exp_peptides.append(pept + [mass])
    return exp_peptides
    