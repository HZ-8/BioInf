import ReadTextPattern, ProfileMostProbableKMer

Text, k, profile = ReadTextPattern.ReadTextPattern('dataset_159_3.txt')
k = int(k)

#print k, d, dna

pat = ProfileMostProbableKMer.ProfileMostProbableKMer(Text, k, profile)

print pat
