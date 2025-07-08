class node:
    def __init__(self, value):
        self.value=value 
        self.children=[]
    def add_child(self, child_node):
        self.children.append(child_node)
    def print_tree(self, level=0):
        print(" " * level + f"- {self.value}")
        for child in self.children:
            child.print_tree(level + 1)
    def get_degree(self):
        return len(self.children)
    def get_height(self):
        if not self.children:
            return 1
        return 1 + max(child.get_height() for child in self.children)
root = node("A")
node_B = node("B")
node_C = node("C")
node_D = node("D")
node_E = node("E")
node_F = node("F")
node_G = node("G")

root.add_child(node_B)
root.add_child(node_C)

node_B.add_child(node_D)
node_B.add_child(node_E)

node_C.add_child(node_F)
node_F.add_child(node_G)

print("struktur tree:")
root.print_tree()

print(f"\nderajat node B: {node_B.get_degree()}")
print(f"derajat node B: {node_B.get_degree()}")
print(f"derajat node F: {node_F.get_degree()}")
print(f"derajat node G: {node_G.get_degree()}")

print(f"\ntinggi pohon dari root A: {root.get_height()}")