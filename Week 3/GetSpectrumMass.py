def GetSpectrumMass(sub_peptide):
    mass = 0
    for number in sub_peptide:
        mass = mass + number
    
    return mass