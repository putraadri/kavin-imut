class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

# Membuat node
node1 = Node(15)
node2 = Node(25)
node3 = Node(35)

# Menyambungkan node
node1.next = node2
node2.next = node3

# Fungsi mencetak isi linked list
def print_list(head):
    current = head
    while current is not None:
        print(f"[{current.data}]", end=" → ")
        current = current.next
    print("None")

# Cetak dari node pertama (head)
print_list(node1)
