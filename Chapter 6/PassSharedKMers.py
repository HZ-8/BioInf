import ReadShared, SharedKMers, WriteArrayToFile

#k, G1, G2 = ReadShared.ReadTextPattern('dataset_289_5 (1).txt')
#k = int(k)

k = 3
G1 = 'TGGCCTGCACGGTAG'
G2 = 'GGACCTACAAATGGC'
res = SharedKMers.SharedKMersList(k, G1, G2)
print len(res)
WriteArrayToFile.WriteArrayToFile(res)
