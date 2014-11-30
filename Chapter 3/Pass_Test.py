import ReadTextPattern, MotifSearch, WriteArrayToFile, random, math

'''k, t, N, dna = ReadTextPattern.ReadTextPattern('dataset_163_4.txt')

k = int(k)
t = int(t)
N = int(N)

bestresult = []
bestscore = k*t + 1

for i in range (20):
    result, score = MotifSearch.GibbsSampler(dna, k, t, N)
    if score < bestscore:
        bestresult = result
        bestscore = score
WriteArrayToFile.WriteArrayToFile(bestresult, bestscore, 'result.txt')
print bestresult, bestscore'''

'''ent = 0
rec = [0.25, 0, 0.5, 0.25]
for el in rec:
    if el <> 0:
        ent -= el * math.log(el)
print rec, ent'''

prof = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9], 'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1], 'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0], 'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
pat = CAGTGA
pat_probab = 1
for j in range(k):
    pat_probab = pat_probab * profile[pattern[j]][j]
    probab_array.append(pat_probab)