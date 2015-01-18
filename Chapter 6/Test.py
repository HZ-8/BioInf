f = open('Test data3.txt', 'r')
ar = []
for line in f:
    ar.append(line)

f.close()

print ar
print len(ar)