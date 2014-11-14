import SpectralConvolution as sc, FrequentElements as fel, \
       LeaderboardCycloPeptideSequencing as ls

def ConvolutionCyclopeptideSequencing(M, N, Spectrum):
    convol = sc.SpectralConvolution(Spectrum)
    convol.sort()
    
    pos = 0
    while (convol[pos] < 57):
        pos += 1
    
    new_convol = convol[pos:]
    FreqAminoList = fel.FrequentElement(new_convol, M)
    
    LeaderPeptide = ls.LeaderboardCycloPeptideSequencing(Spectrum, N, FreqAminoList)
    
    return LeaderPeptide