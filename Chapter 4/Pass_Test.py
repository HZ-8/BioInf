import ReadTextPattern, WriteArrayToFile, ReconstructString

#Patterns = ReadTextPattern.ReadTextPattern('dataset_203_6.txt')
#k = int(k)
k = 8
path = ReconstructString.KUniversalCircularString(k)

'''sorted_graph = {}
keys2 = graph.keys()
keys2.sort()
for el in keys2: sorted_graph[el] = graph[el]'''
#print path
WriteArrayToFile.WriteArrayToFile(path)

'''bin3 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(3)]))
bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)]))

dic = []
for i in range(2 ** 3):    
    s = bin3(i)
    dic.append(s)

dic.sort()
print dic 

#count = 0
for i in range(2 ** 8):    
    s = bin8(i)
    temp = []    
    for j in range(6):
        temp.append(s[j:j+3])
    t = s[6:8] + s[0]
    temp.append(t)
    t = s[7] + s[0:2]
    temp.append(t)  
    temp.sort()
    
    if dic == temp:
        #count +=1
        print s
#print count'''
