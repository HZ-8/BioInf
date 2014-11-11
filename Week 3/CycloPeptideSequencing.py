import Expand as exp, GetSpectrumMass as gm, \
GenerateNumSubPeptides as gn, SpectrumMatch as sm, \
 GenerateLinNumSubPeptides as gln

def CycloPeptideSequencing(Spectrum, dict_18):
    '''Return a list of peptides which have Spectrum'''
    result = []
    Peptides = [0]
    pmass = max(Spectrum)
    while len(Peptides) > 0:
        Peptides = exp.Expand(Peptides, dict_18)
        final_pept = []

        for Peptide in Peptides:
            if gm.GetSpectrumMass(Peptide) == pmass:
                pept_spectr = gn.GenerateNumSubPeptides(Peptide)
                if sm.SpectrumMatch(pept_spectr, Spectrum):
                    result.append(Peptide)
            else:
                line_sp = gln.GenerateLinNumSubPeptides(Peptide)
                if sm.SpectrumMatch(line_sp, Spectrum):
                    final_pept.append(Peptide)
                
        Peptides = final_pept  
    return result