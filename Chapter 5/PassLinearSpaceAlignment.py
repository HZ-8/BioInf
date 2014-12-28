import LinearSpaceAlignment, ReadTextPattern #, WriteArrayToFile

Score = ReadTextPattern.ReadScoreMatrix('BLOSUM62 Score Matrix.txt')
sigma = 5

v, w = ReadTextPattern.ReadTextPattern('Test data.txt')
n = len(v)
m = len(w)
res = LinearSpaceAlignment.LinearSpaceAlignment(v, w, Score, sigma)
print res

p1, p2 = LinearSpaceAlignment.GetPath(v, w, res)

print p1
print p2

score = 0
for i in range(len(p1)):
    if p1[i] == '-' or p2[i] == '-':
        score -= sigma
    else:
        score += Score[p1[i]][p2[i]]

print score

#print path1
#print path2
#WriteArrayToFile.WriteArrayToFile([path1, path2])