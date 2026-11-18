class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the Binary Tree using TEMPORADA and Gabriela
root = Node("E")

# Left subtree
root.left = Node("L")
root.left.left = Node("I")
root.left.right = Node("A")

root.left.left.left = Node("R")
root.left.left.right = Node("E")

root.left.left.left.left = Node("A")
root.left.left.left.left.left = Node("G")
root.left.left.left.left.right = Node("B")

root.left.right.right = Node("T")


# Right subtree
root.right = Node("M")
root.right.left = Node("P")
root.right.right = Node("D")

root.right.left.left = Node("O")
root.right.left.left.left = Node("R")
root.right.left.left.right = Node("A")

root.right.right.right = Node("A")


# Preorder Traversal: Root - Left - Right
def preorder(node):
    if node:
        print(node.data, end=" - ")
        preorder(node.left)
        preorder(node.right)


# Inorder Traversal: Left - Root - Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" - ")
        inorder(node.right)


# Postorder Traversal: Left - Right - Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" - ")


# Display the traversal results
print("DFS METHODS IN BINARY TREE: TEMPORADA")

print("\nPreorder (Root - Left - Right):")
preorder(root)

print("\n\nInorder (Left - Root - Right):")
inorder(root)

print("\n\nPostorder (Left - Right - Root):")
postorder(root)

print()
