def PeptidePositions(translation, peptide):
    ''' RNA is translated whole; find positions where peptide starts'''
    positions = []
    i = 0
    while i <= len(translation)-len(peptide) +1:
        pos = translation.find(peptide, i)
        if pos == -1:
            return positions
        positions.append(pos)
        i = pos + 1
    return positions