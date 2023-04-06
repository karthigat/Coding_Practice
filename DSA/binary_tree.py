class Tree():
    def __init__(self, data):
        self.childern = []
        self.parent = None
        self.data = data

    def add_child(self, child):
        print(self)
        child.parent = self
        self.childern.append(child)

    def display(self):
        print(self.data)
        print(self.right)
        print(self.left)
        if len(self.childern) > 0:
            for child in self.childern:
                print(child.data)
                
def build_tree():
    root = Tree('a')
    a = Tree('b')
    a.add_child(Tree('c'))
    a.add_child(Tree('d')) 

    # e = Tree('e')
    # node_d = Tree('d')
    # node_e = Tree('e')
    # node_f = Tree('f')

    # node_a.left = 'b'
    # node_a.right = 'c'
    # node_b.left = 'd'
    # node_b.right = 'e'
    # node_c.right = 'f'

    # print(node_a.display())
    return root

if __name__ == '__main__':
    root = build_tree()
    root.display()