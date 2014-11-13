import SpectralConvolution as sc

def ConvolutionCyclopeptideSequencing(M, N, Spectrum):
    convol = sc.SpectralConvolution(Spectrum)
    
    exper_masses = []
    count = 0
    i = 0
    while (i < len(convol)) and (count < M):
        if convol[i] >= 57:
            count += 1
            exper_masses.append(convol[i])
            i += 1
            while (convol[i] == convol[i-1]) and (i < len(convol)):
                exper_masses.append(convol[i])
                i += 1
    
                
                
        