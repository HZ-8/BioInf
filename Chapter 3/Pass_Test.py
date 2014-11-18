import ReadTextPattern, MotifEnumeration, WriteArrayToFile

k, d, dna = ReadTextPattern.ReadTextPattern('dataset_156_7.txt')
k = int(k)
d = int(d)

#print k, d, dna

motifs = MotifEnumeration.MotifEnumeration(dna, k, d)

WriteArrayToFile.WriteArrayToFile(motifs, 'result.txt')
