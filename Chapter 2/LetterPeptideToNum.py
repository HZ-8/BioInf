def LetterPeptideToNum(Peptide, MassDict):
    ''' Take a letter representation of a peptide, and return number
    representation'''
    numPeptide = []
    for let in Peptide:
        numPeptide.append(MassDict[let])

    return numPeptide