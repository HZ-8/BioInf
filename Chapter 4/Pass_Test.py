import ReadTextPattern, WriteArrayToFile, StringComposition

pat = ReadTextPattern.ReadTextPattern('dataset_198_9.txt')

#k = int(k)
result = StringComposition.OverlapGraph(pat)
#print result
WriteArrayToFile.WriteArrayToFile(result)