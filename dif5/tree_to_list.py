class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tr):
    tab=[]
    tab.append(tr.data)
    print(tab)
    return tab.sort()






print(tree_to_list(Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6)]), Node(7)])))