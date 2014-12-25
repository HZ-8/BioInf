import EditDistance, ReadTextPattern, WriteArrayToFile

v, w = ReadTextPattern.ReadTextPattern('dataset_248_3.txt')
n = len(v)
m = len(w)

pathscore = EditDistance.EditAlignment(v, w)

print pathscore
'''
path1 =  GlobalAlignment.OutputAlignment(path_g, v, n-1, m-1, 1)
path2 =  GlobalAlignment.OutputAlignment(path_g, w, n-1, m-1, 2)

#print path1, path2
WriteArrayToFile.WriteArrayToFile([path1, path2])'''