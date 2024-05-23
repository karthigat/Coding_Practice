# DFS - using recursive method

graph = {
    'A':['B','C'], 'B':['D'], 'C':['D','E'], 'D':['E'], 'E':['F'], 'F':[]
}

visited = list()
def DFS_algo(visited, graph, root):
    if root not in visited: 
        visited.append(root)
        for neighbour in graph[root]:
            DFS_algo(visited, graph, neighbour)
    return visited
print(DFS_algo(visited, graph, 'A'))