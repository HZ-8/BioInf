import GenerateSubPeptides as gsp, GetSubPeptideMass as gsm

def GenerateTheoreticalSpectrum(Peptide, aamass):
    '''Take a peptide and return a list of masses of its subparts'''
    spectr =[0]
    parts = gsp.GenerateSubPeptides(Peptide)
    
    for part in parts:
        spectr.append(gsm.GetSubPeptideMass(part, aamass))
    
    spectr.sort()
    
    return spectr