def GetNumPeptideMass(numPeptide):
    '''Add all values together of a given num peptide'''
    mass = 0
    for number in numPeptide:
        mass = mass + number
    
    return mass