import ReadTextPattern, WriteArrayToFile, ReconstructString

AdjList = ReadTextPattern.ReadTextPattern('dataset_203_2 (1).txt')

#k = int(k)
path = ReconstructString.EulerianCycle(AdjList)

'''sorted_graph = {}
keys2 = graph.keys()
keys2.sort()
for el in keys2: sorted_graph[el] = graph[el]'''
#print path
WriteArrayToFile.WriteArrayToFile(path)

'''bin4 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(4)]))
bin19 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(19)]))

dic = []
for i in range(2 ** 4):    
    s = bin4(i)
    dic.append(s)

dic.sort()
print dic 

count = 0
for i in range(2 ** 19):    
    s = bin19(i)
    
    temp = []    
    for j in range(16):
        temp.append(s[j:j+4])
    temp.sort()
    
    if dic == temp:
        count +=1
print count'''
