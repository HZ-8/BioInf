import SpectralConvolution as sc, FrequentElements as fel, \
       LeaderboardCycloPeptideSequencing as ls

def ConvolutionCyclopeptideSequencing(M, N, Spectrum):
    convol = sc.SpectralConvolution(Spectrum)

    FreqAminoList = fel.FrequentElement(convol, M)
    print 'FreqAminoList', FreqAminoList
    
    LeaderPeptide = ls.LeaderboardCycloPeptideSequencing(Spectrum,
                                                         N, FreqAminoList)
    
    return LeaderPeptide