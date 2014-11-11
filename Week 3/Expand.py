def Expand(numPeptides, mass_dictionary):
    '''Take a list of numeric peptides, and return expanded list (added one 
    mass from dictionary to the end of each peptide, getting 18x records)'''
    exp_peptides = []
    
    if numPeptides == [0]:
        for key in mass_dictionary:
            exp_peptides.append([mass_dictionary[key]])
        return exp_peptides
    
    for pept in numPeptides:
        for key in mass_dictionary:
            exp_peptides.append(pept + [mass_dictionary[key]])
    return exp_peptides
    