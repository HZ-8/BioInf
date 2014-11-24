import ReadTextPattern, ProfileMostProbableKMer

Text, k, profile = ReadTextPattern.ReadTextPattern('dataset_159_3.txt')

k = int(k)

median = DistanceBetweenPatternAndStrings.MedianString(dna, k)

print median

pat = ProfileMostProbableKMer.ProfileMostProbableKMer(Text, k, profile)

print pat
