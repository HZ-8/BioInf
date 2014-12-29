import MultipleSubsequence, ReadTextPattern, WriteArrayToFile

'''v1 = 'ATATCCG'
v2 = 'TCCGA'
v3 = 'ATGTACTG'''

v1 = 'ATA'
v2 = 'TC'
v3 = 'ATGT'

#v1, v2, v3 = ReadTextPattern.ReadTextPattern('dataset_247_3.txt')

score, path_g = MultipleSubsequence.MultipleAlignment(v1, v2, v3)

#print score
print path_g

#path1, path2, path3 = MultipleSubsequence.OutputLCS(path_g, v1, v2, v3)
backtrack = MultipleSubsequence.OutputLCS(path_g, v1, v2, v3)

print backtrack
#WriteArrayToFile.WriteArrayToFile([path1, path2])'''