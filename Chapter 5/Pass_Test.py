#import StringComposition
n = 17
m = 13
'''nodes = []
node = 0
for i in range (n):
    row = []
    for j in range(m):
       row.append(node)
       node +=1
    nodes.append(row)

graph = {}      
for i in range (n-1):
    for j in range(m-1):
        node = nodes[i][j]
        graph[node] = [nodes[i][j+1], nodes[i+1][j]]

for i in range(n-1):
    node = nodes[i][m-1]
    graph[node] = [nodes[i+1][m-1]]
    
for j in range (m-1):
    node = nodes[n-1][j]
    graph[node] = [nodes[n-1][j+1]]

def Paths(node):
    if node == 0:
        paths = []
    if node in graph:
        for way in graph[node]:
            Paths(way)
    else:
       return paths '''
'''nodes = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(0)
    nodes.append(row)
for i in range(n):
    nodes[i][0] = 1
for j in range(m):
    nodes[0][j] = 1    

for j in range(1, m):
    for i in range(1, n):
        nodes[i][j] = nodes[i][j-1] + nodes[i-1][j]

print nodes[n-1][m-1]'''

s = 1.0 / 2
for i in range (8):
    for j in range(8):
        s = s * 2
        
print s