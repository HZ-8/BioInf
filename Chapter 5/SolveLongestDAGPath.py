def PathWeight(start_node, graph):
    '''From a graph containing sets
    {in_node: [[out_node1, weight1], [out_node2, weight2]]}, form a
    graph that contains sets {node: [node from longest path, path length]}'''
    
    wait_list = [start_node]
    path_graph = {}
    
    while wait_list <> []:
        node = wait_list[0]
        if node == start_node:
            weight = 0
        else:
            weight = path_graph[node][1]
            
        if node not in graph:
            wait_list.remove(node)
            continue
        for array in graph[node]:
            in_node = array[0]
            wait_list.append(in_node)
            if in_node in path_graph:
                if array[1] + weight > path_graph[in_node][1]:
                   path_graph[in_node][0] = node
                   path_graph[in_node][1] = array[1] + weight
            else:
                path_graph[in_node] = [node, array[1] + weight]
        wait_list.remove(node)
        
    return path_graph

def GetPath(path_graph, start_node, end_node):
    '''Having a graph with all nodes and path length-origin for each of them, 
    get the way from enf to start node'''
    
    path = [end_node]
    node = end_node
    
    while node <> start_node:
        node = path_graph[node][0]
        path = [node] + path
        
    return path