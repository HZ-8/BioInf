import GenerateLinNumSubPeptides as gsp

def GenerateLinTheoreticalSpectrum(numPeptide):
    '''Take a numeric peptide and return its linear spectrum'''
    spectr = gsp.GenerateLinNumSubPeptides(numPeptide)

    spectr.sort()

    return spectr