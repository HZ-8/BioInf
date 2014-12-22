import SolveLongestCommonSubsequence, ReadTextPattern

v, w = ReadTextPattern.ReadTextPattern('dataset_245_5.txt')

b = SolveLongestCommonSubsequence.LCSBackTrack(v, w)
s = SolveLongestCommonSubsequence.OutputLCS(b, v, len(v)-1, len(w)-1)

print s