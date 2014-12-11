import ReadTextPattern, WriteArrayToFile, StringComposition, ReconstructString

#k, d, Patterns = ReadTextPattern.ReadTextPattern('dataset_204_14.txt')
#k = int(k)
#d = int(d)
k = 3
d = 1
pat = [['ACC', 'ATA'],
 ['ACT', 'ATT'],
 ['ATA', 'TGA'],
 ['ATT', 'TGA'],
 ['CAC', 'GAT'],
 ['CCG', 'TAC'],
 ['CGA', 'ACT'],
 ['CTG', 'AGC'],
 ['CTG', 'TTC'],
 ['GAA', 'CTT'],
 ['GAT', 'CTG'],
 ['GAT', 'CTG'],
 ['TAC', 'GAT'],
 ['TCT', 'AAG'],
 ['TGA', 'GCT'],
 ['TGA', 'TCT'],
 ['TTC', 'GAA']]

graph = StringComposition.DeBruijnFromPatternsPairs(Patterns)
node_path = ReconstructString.EulerianPath(graph)
pairs = []
for i in range(len(node_path)):
    pairs.append([node_path[i][:k-1], node_path[i][k-1:]])

path = StringComposition.StringSpelledByPairs(pairs, k, d)

print path
#WriteArrayToFile.WriteArrayToFile(path)