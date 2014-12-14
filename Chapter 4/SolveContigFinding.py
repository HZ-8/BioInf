import ReadTextPattern, WriteArrayToFile, StringComposition

Patterns = ReadTextPattern.ReadTextPattern('dataset_205_5 (1).txt')
graph = StringComposition.DeBruijnFromPatterns(Patterns)
contigs = StringComposition.NonBranchingPaths(graph)
WriteArrayToFile.WriteArrayToFile(contigs)