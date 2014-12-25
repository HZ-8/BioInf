'''import SolveLongestCommonSubsequence, ReadTextPattern

v, w = ReadTextPattern.ReadTextPattern('dataset_245_5.txt')

b = SolveLongestCommonSubsequence.LCSBackTrack(v, w)
s = SolveLongestCommonSubsequence.OutputLCS(b, v, len(v)-1, len(w)-1)

print s'''

'''import SolveLongestDAGPath, ReadTextPattern, WriteArrayToFile

sn, en, graph = ReadTextPattern.ReadTextPattern('dataset_245_7.txt')

path_g = SolveLongestDAGPath.PathWeight(sn, graph)
print path_g[en][1]
path = SolveLongestDAGPath.GetPath(path_g, sn, en)

WriteArrayToFile.WriteArrayToFile(path)'''

import GlobalAlignment, ReadTextPattern, WriteArrayToFile

Score = ReadTextPattern.ReadScoreMatrix('BLOSUM62 Score Matrix.txt')
sigma = 5
#v = 'PLEASANTLY'
#w = 'MEANLY'

v, w = ReadTextPattern.ReadTextPattern('dataset_247_3.txt')
n = len(v)
m = len(w)

pathscore, path_g = GlobalAlignment.GlobalAlignment(v, w, Score, sigma)

print pathscore

path1 =  GlobalAlignment.OutputAlignment(path_g, v, n-1, m-1, 1)
path2 =  GlobalAlignment.OutputAlignment(path_g, w, n-1, m-1, 2)

#print path1, path2
WriteArrayToFile.WriteArrayToFile([path1, path2])