from . import Node, Tree

class nary_Node(Node):
    def __init__(self, content, children = []):
        self.content = content
        self.children = children
        #self.roots =
class nary_Tree(Tree):
    def __init__(self, root = None):
        self.root = root

    def add_Node(self, node):
        if self.root:
            if !self.is_Full(self.root.left):
                self.root.left.append(node)
            elif !self.is_Full(self.root.right):
                self.root.right.append(node)
            else:
                self.root.left.add_Node()
        else:
            self.root = node
    def remove_Node(self, node):

    def is_Full(self,node):
        return len(node.children) == self.n
