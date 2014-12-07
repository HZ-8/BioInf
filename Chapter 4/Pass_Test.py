import ReadTextPattern, WriteArrayToFile, StringComposition

Patterns = ReadTextPattern.ReadTextPattern('dataset_200_7.txt')

#k = int(k)
graph = StringComposition.DeBruijnFromPatterns(Patterns)

'''sorted_graph = {}
keys2 = graph.keys()
keys2.sort()
for el in keys2: sorted_graph[el] = graph[el]'''
print graph
WriteArrayToFile.WriteArrayToFile(graph)

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
