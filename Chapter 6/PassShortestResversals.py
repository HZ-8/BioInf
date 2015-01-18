import BreakpointGraph, ReadTextPattern, WriteReversalsToFile

P, Q = ReadTextPattern.ReadTextPattern('dataset_288_5.txt')
#P = [[1, -7, 6,-10, 9, -8, 2, -11, -3, 5, 4]]
#Q = [[1, 2,3,4,5,6,7,8,9,10, 11]]
#Solve distance

#Red = BreakpointGraph.ColoredEdges(P)
#print len(Red)
#Blue = BreakpointGraph.ColoredEdges(Q)
'''blocks = len(Red)
c = BreakpointGraph.CycleCount(Red, Blue)
print c'''

#Return reversals
#Red = BreakpointGraph.ColoredEdgesGraph(P)
#Blue = BreakpointGraph.ColoredEdgesGraph(Q)

rev = BreakpointGraph.ShortestRearrangementGraph(P, Q)
WriteReversalsToFile.WriteReversalsToFile(rev)
'''P1 = rev[-1]
Red = BreakpointGraph.ColoredEdges(P1)
Blue = BreakpointGraph.ColoredEdges(Q)
blocks = len(Red)
c = BreakpointGraph.CycleCount(Red, Blue)
print c'''

'''for el in rev:
    print el'''