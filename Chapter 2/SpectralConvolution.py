def SpectralConvolution(Spectrum, start_mass = 57, end_mass = 200):
    '''For a spectrum, return a list of its convolutions
    (all ith-jth elements), which by default are greater than zero '''
    convolution = []
    
    Spectrum.sort()
    for i in range (1, len(Spectrum)):
        for j in range (len(Spectrum)):
            diff = Spectrum[i] - Spectrum[j]
            if start_mass <= diff <= end_mass:
                convolution.append(diff)
    return convolution