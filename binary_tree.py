
from collections import deque

# Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the Binary Tree
root = Node("T")

root.left = Node("E")
root.right = Node("M")

root.left.left = Node("P")
root.left.right = Node("O")

root.right.left = Node("R")
root.right.right = Node("A1")

root.left.left.left = Node("D")
root.left.left.right = Node("A2")


# Breadth-First Search (BFS)
def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


# Depth-First Search (DFS) - Preorder
def dfs(root):
    if root is None:
        return []

    result = [root.data]
    result += dfs(root.left)
    result += dfs(root.right)

    return result


# Display the results
print("BINARY TREE: TEMPORADA")

print("\nBFS (Breadth-First Search):")
print(" - ".join(bfs(root)))

print("\nDFS (Depth-First Search):")
print(" - ".join(dfs(root)))
