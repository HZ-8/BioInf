import Expand as exp, ParentMass as pm, GetSpectrumMass as gm, \
GenerateNumSubPeptides as gn, SpectrumMatch as sm, \
 GenerateLinNumSubPeptides as gln

def CycloPeptideSequencing(Spectrum, dict_18):
    result = []
    Peptides = [0]
    pmass = pm.ParentMass(Spectrum)
    #while len(Peptides) > 0:
    for i in range(10):
        Peptides = exp.Expand(Peptides, dict_18)
        final_pept = []

        for Peptide in Peptides:
            if gm.GetSpectrumMass(Peptide) == pmass:
                pept_spectr = gn.GenerateNumSubPeptides(Peptide)
                if sm.SpectrumMatch(pept_spectr, Spectrum):
                    result.append(Peptide)
            else:
                #if sm.SpectrumMatch(Peptide, Spectrum):
                line_sp = gln.GenerateLinNumSubPeptides(Peptide)
                if sm.SpectrumMatch(line_sp, Spectrum):
                    final_pept.append(Peptide)
                
        Peptides = final_pept  
    return result