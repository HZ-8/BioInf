import ReadTextPattern, WriteArrayToFile, StringComposition

pat = ReadTextPattern.ReadTextPattern('dataset_198_9.txt')

#k = int(k)
result = StringComposition.OverlapGraph(pat)
#print result
WriteArrayToFile.WriteArrayToFile(result)

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
