import ReadTextPattern, GreedyMotifSearch, WriteArrayToFile

k, t, dna = ReadTextPattern.ReadTextPattern('dataset_160_9.txt')

k = int(k)
t = int(t)

result = GreedyMotifSearch.GreedyMotifSearch(dna, k, t)
WriteArrayToFile.WriteArrayToFile(result)
