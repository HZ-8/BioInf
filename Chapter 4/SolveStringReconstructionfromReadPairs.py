import ReadTextPattern, WriteArrayToFile, StringComposition, ReconstructString

k, d, Patterns = ReadTextPattern.ReadTextPattern('Test_data.txt')
k = int(k)
d = int(d)
#k = 8
graph = StringComposition.DeBruijnFromPatternsPairs(Patterns)
node_path = ReconstructString.EulerianPath(graph)
pairs = []
for i in range(len(node_path)):
    pairs.append([node_path[:k], node_path[k:]])

path = StringComposition.StringSpelledByPairs(pairs, d)

print path
#WriteArrayToFile.WriteArrayToFile(path)