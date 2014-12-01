import ReadTextPattern, WriteArrayToFile, StringComposition

k, Text = ReadTextPattern.ReadTextPattern('dataset_197_3.txt')

k = int(k)
result = StringComposition.StringComposition(Text, k)

WriteArrayToFile.WriteArrayToFile(result)