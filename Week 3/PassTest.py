import SpectralConvolution as sc, WriteArrayToFile, ReadTextPattern as rp


#massdict = aam.AminoAcidMasses()
#dict_18 = aam.AminoAcidMasses('united_integer_mass_table.txt')

spect = rp.ReadTextPattern('dataset_104_4.txt')

cycl = sc.SpectralConvolution(spect)
cycl.sort()

WriteArrayToFile.WriteArrayToFile(cycl)
