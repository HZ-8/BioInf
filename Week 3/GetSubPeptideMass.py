def GetSubPeptideMass(sub_peptide, aa_mass):
    masses = aa_mass
    mass = 0
    for letter in sub_peptide:
        mass = mass + masses[letter]
    
    return mass