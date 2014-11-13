def SpectralConvolution(Spectrum):
    '''For a spectrum, return a sorted list of its convolutions
    (all ith-jth elements)'''
    convolution = []
    
    Spectrum.sort()
    for i in range (1, len(Spectrum)):
        for j in range (len(Spectrum)):
            diff = Spectrum[i] - Spectrum[j]
            if diff > 0:
                convolution.append(diff)
    return convolution