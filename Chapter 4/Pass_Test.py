'''import ReadTextPattern, WriteArrayToFile, StringComposition, ReconstructString

k, d, Patterns = ReadTextPattern.ReadTextPattern('Test_data.txt')
k = int(k)
d = int(d)
#k = 8
path = StringComposition.StringSpelledByPairs(Patterns, d)
#path = ReconstructString.StringReconstruction(Patterns)'''

'''sorted_graph = {}
keys2 = graph.keys()
keys2.sort()
for el in keys2: sorted_graph[el] = graph[el]'''
#print path
#WriteArrayToFile.WriteArrayToFile(path)

bin3 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(3)]))
bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)]))

dic = []
for i in range(2 ** 3):    
    s = bin3(i)
    dic.append(s)

dic.sort()
#print dic

#count = 0
#for i in range(2 ** 8):    
#s = bin8(i)
s = '1001101100'
temp = []    
for j in range(8):
    temp.append(s[j:j+3])
'''t = s[6:8] + s[0]
temp.append(t)
t = s[7] + s[0:2]
temp.append(t)'''
print temp  
temp.sort()

if dic == temp:
    #count +=1
    print 'Yes'
else:
    print 'No'
#print count
'''
AdjList = {1: [2,3,5], 2: [1,4], 3: [2,5], 4: [1,2,5], 5: [3,4]}    
nodes = {}
for key in AdjList:
    for value in AdjList[key]:
        if value in nodes:
            nodes[value] += 1
        else:
            nodes[value] = 1
        if key in nodes:
            nodes[key] -= 1
        else:
            nodes[key] = -1
print nodes'''