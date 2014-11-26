import ReadTextPattern, MotifSearch, WriteArrayToFile

k, t, dna = ReadTextPattern.ReadTextPattern('dataset_161_5 (2).txt')

k = int(k)
t = int(t)

bestresult = []
bestscore = k*t + 1

for i in range (1000):
    result, score = MotifSearch.RandomizedMotifSearch(dna, k, t)
    if score < bestscore:
        bestresult = result
        bestscore = score
WriteArrayToFile.WriteArrayToFile(bestresult, bestscore, 'result.txt')
#print bestresult, bestscore
