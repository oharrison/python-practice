class Tree:
    def __init__(self, root):
        assert type(root) == Node
        self.root = root

    def print_tree(self):
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                print(node.get_data(), end="\t")
                if node.has_children():
                    for child_node in node.get_children():
                        next_level.append(child_node)
            print()
            if next_level:
                current_level = [node for node in next_level]
            else:
                current_level = None

    def recurse_print(self, current_level):
        if current_level == None:
            return
        else:
            next_level = []
            for node in current_level:
                print(node.get_data(), end="\t")
                if node.has_children():
                    for child_node in node.get_children():
                        next_level.append(child_node)
            print()
            if next_level:
                current_level = next_level
            else:
                current_level = None

            self.recurse_print(current_level)

class Node:
    def __init__(self, data, children = None):
        assert children == None or type(children) == list
        assert data != None
        self.data = data
        self.children = children

    def has_children(self):
        if self.children != None:
            return True
        return False

    def get_children(self):
        return self.children

    def set_children(self, new_children):
        assert type(new_children) == list and len(new_children) > 0
        self.children = new_children

    def get_data(self):
        return self.data


if __name__ == '__main__':

    # create tree
    root_node = Node(1)
    root_node.set_children([Node(2, [Node(4, [Node(8)]), Node(5), Node(6)]), Node(3, [Node(7, [Node(9), Node(10)])])])
    tree = Tree(root_node)

    # iterative print
    tree.print_tree()

    # recursive print
    tree.recurse_print([root_node])
