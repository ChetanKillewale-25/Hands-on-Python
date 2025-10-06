# DFS in Python

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = dfs(graph, 'A', [])
print(visited)


# BFS in Python

def bfs(graph, root):
    visited = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([x for x in graph[node] if x not in visited])

    return visited

"""graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
"""
visited = bfs(graph, 'A')
print(visited)
