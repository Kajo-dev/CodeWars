from platform import node


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

print(Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6)]), Node(7)]))

print(Node.data[1])