def Expand(Peptides, mass_dictionary):
    exp_peptides = []
    
    if Peptides == [0]:
        for key in mass_dictionary:
            exp_peptides.append([mass_dictionary[key]])
        return exp_peptides
    
    for pept in Peptides:
        for key in mass_dictionary:
            exp_peptides.append(pept + [mass_dictionary[key]])
    return exp_peptides
    