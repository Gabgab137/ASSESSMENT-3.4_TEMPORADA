
# Graph representation of TEMPORADA
# The graph is undirected.

graph = {
    "T": ["E", "M"],
    "E": ["T", "P", "O"],
    "M": ["T", "R", "A1"],
    "P": ["E", "D", "R"],
    "O": ["E", "A2"],
    "R": ["M", "P", "D"],
    "A1": ["M", "A2"],
    "D": ["P", "R", "A2"],
    "A2": ["O", "A1", "D"]
}


# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = []
    queue = [start]

    visited.append(start)

    while queue:
        vertex = queue.pop(0)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited


# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# Display the results
print("GRAPH: TEMPORADA")

print("\nBFS (Breadth-First Search):")
print(" - ".join(bfs(graph, "T")))

print("\nDFS (Depth-First Search):")
print(" - ".join(dfs(graph, "T")))
