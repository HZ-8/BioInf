import OverlapAlignment, ReadTextPattern, WriteArrayToFile

sigma = 2

v, w = ReadTextPattern.ReadTextPattern('dataset_248_7.txt')

n = len(v)
m = len(w)

pathscore, sink, path_g = OverlapAlignment.OverlapAlignment(v, w, sigma)

print pathscore
#print sink
#print path_g

path1 = OverlapAlignment.OverlapPath(path_g, v, sink[0]-1, sink[1]-1, 1)
path2 = OverlapAlignment.OverlapPath(path_g, w, sink[0]-1, sink[1]-1, 2)

#print path1
#print path2

WriteArrayToFile.WriteArrayToFile([path1, path2])