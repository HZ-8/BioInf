import AminoAcidMasses as aam, LeaderboardCycloPeptideSequencing as lcs

massdict = aam.AminoAcidMasses()
dict_18 = aam.AminoAcidMasses('united_integer_mass_table.txt')

spect = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
N = 10

leadpept = lcs.LeaderboardCycloPeptideSequencing(spect, N, dict_18)
print leadpept