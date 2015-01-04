import GreedySorting, ReadTextPattern, WriteArrayToFile

P = ReadTextPattern.ReadTextPattern('dataset_286_3.txt')

steps, reversals = GreedySorting.GreedySorting(P)

WriteArrayToFile.WriteArrayToFile(reversals)