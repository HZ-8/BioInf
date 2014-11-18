def GetPeptideMass(Peptide, aa_dictionary):
    '''Get mass of a letter-represented peptide, with the help of 20-element
    dictionary'''
    masses = aa_dictionary
    mass = 0
    for letter in Peptide:
        mass = mass + masses[letter]
    
    return mass