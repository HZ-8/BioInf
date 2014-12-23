'''import SolveLongestCommonSubsequence, ReadTextPattern

v, w = ReadTextPattern.ReadTextPattern('dataset_245_5.txt')

b = SolveLongestCommonSubsequence.LCSBackTrack(v, w)
s = SolveLongestCommonSubsequence.OutputLCS(b, v, len(v)-1, len(w)-1)

print s'''

import SolveLongestDAGPath, ReadTextPattern, WriteArrayToFile

sn, en, graph = ReadTextPattern.ReadTextPattern('dataset_245_7.txt')

path_g = SolveLongestDAGPath.PathWeight(sn, graph)
print path_g[en][1]
path = SolveLongestDAGPath.GetPath(path_g, sn, en)

WriteArrayToFile.WriteArrayToFile(path)