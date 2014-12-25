import EditDistance, ReadTextPattern #, WriteArrayToFile

v, w = ReadTextPattern.ReadTextPattern('Test data.txt')
print v
print w

n = EditDistance.EditDistance(v, w)
print n