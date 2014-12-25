import LocalAlignment, ReadTextPattern, WriteArrayToFile

Score = ReadTextPattern.ReadScoreMatrix('PAM250 Score Matrix.txt')
sigma = 5

v, w = ReadTextPattern.ReadTextPattern('dataset_247_9 (1).txt')

n = len(v)
m = len(w)

pathscore, sink, path_g = LocalAlignment.LocalAlignment(v, w, Score, sigma)

print pathscore
#print sink
#print path_g

path1 =  LocalAlignment.OutputAlignment(path_g, v, sink[0]-1, sink[1]-1, 1)
path2 =  LocalAlignment.OutputAlignment(path_g, w, sink[0]-1, sink[1]-1, 2)

#print path1
#print path2

WriteArrayToFile.WriteArrayToFile([path1, path2])