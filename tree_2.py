class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Membuat node dan menyusun tree
root = BinaryNode("A")
root.left = BinaryNode("B")
root.right = BinaryNode("C")
root.left.left = BinaryNode("D")
root.left.right = BinaryNode("E")

# Fungsi preorder traversal
def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

# Menampilkan hasil traversal
print("Binary Tree - Preorder traversal:")
preorder(root)