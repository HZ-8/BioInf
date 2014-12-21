import ReadTextPattern, ManhattenTourist

n, m, Down, Right = ReadTextPattern.ReadTextPattern('dataset_261_9.txt')
n, m = map(int, [n, m])

path_length = ManhattenTourist.ManhattenTourist(n, m, Down, Right)

print path_length