import MultipleSubsequence, ReadTextPattern, WriteArrayToFile

'''v1 = 'ATATCCG'
v2 = 'TCCGA'
v3 = 'ATGTACTG'''

'''v1 = 'ATA'
v2 = 'TC'
v3 = 'ATGT'''

v1, v2, v3 = ReadTextPattern.ReadTextPattern('dataset_251_5.txt')

score, path_g = MultipleSubsequence.MultipleAlignment(v1, v2, v3)

print score
#print path_g

#path1, path2, path3 = MultipleSubsequence.OutputLCS(path_g, v1, v2, v3)
p1, p2, p3 = MultipleSubsequence.OutputLCS(path_g, v1, v2, v3)

print p1
print p2
print p3
#WriteArrayToFile.WriteArrayToFile([path1, path2])'''