import FittingAlignment, ReadTextPattern, WriteArrayToFile

sigma = 1

v, w = ReadTextPattern.ReadTextPattern('dataset_248_5.txt')

n = len(v)
m = len(w)

pathscore, sink, path_g = FittingAlignment.FittingAlignment(v, w, sigma)

print pathscore
#print sink
#print path_g

path1 = FittingAlignment.FittingPath(path_g, v, sink[0]-1, sink[1]-1, 1)
path2 = FittingAlignment.FittingPath(path_g, w, sink[0]-1, sink[1]-1, 2)

#print path1
#print path2

WriteArrayToFile.WriteArrayToFile([path1, path2])