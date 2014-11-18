import SpectralConvolution as sc, WriteArrayToFile, ReadTextPattern as rp


#massdict = aam.AminoAcidMasses()
dict_18 = [71, 103, 115, 129, 147, 57, 137, 113, 131, 114,
           97, 128, 156, 87, 101, 99, 186, 163]


spect = rp.ReadTextPattern('dataset_104_4.txt')

cycl = sc.SpectralConvolution(spect)
cycl.sort()

WriteArrayToFile.WriteArrayToFile(cycl)
