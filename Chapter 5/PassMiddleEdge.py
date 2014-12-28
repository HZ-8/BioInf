import MiddleEdge, ReadTextPattern #, WriteArrayToFile

Score = ReadTextPattern.ReadScoreMatrix('BLOSUM62 Score Matrix.txt')
sigma = 5

v, w = ReadTextPattern.ReadTextPattern('dataset_250_12.txt')
n = len(v)
m = len(w)

s, e = MiddleEdge.MiddleEdge(v, w, Score, sigma)

print s,e

#print path1
#print path2
#WriteArrayToFile.WriteArrayToFile([path1, path2])