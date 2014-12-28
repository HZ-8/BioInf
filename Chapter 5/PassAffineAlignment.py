import AffineAlignment, ReadTextPattern, WriteArrayToFile

Score = ReadTextPattern.ReadScoreMatrix('BLOSUM62 Score Matrix.txt')
sigma = 11
eps = 1

v, w = ReadTextPattern.ReadTextPattern('dataset_249_8 (1).txt')
n = len(v)
m = len(w)

pathscore, path_g = AffineAlignment.AffineAlignment(v, w, Score, sigma, eps)

print pathscore

path1 =  AffineAlignment.OutputAlignment(path_g, v, n-1, m-1, 1)
path2 =  AffineAlignment.OutputAlignment(path_g, w, n-1, m-1, 2)

#print path1
#print path2
WriteArrayToFile.WriteArrayToFile([path1, path2])