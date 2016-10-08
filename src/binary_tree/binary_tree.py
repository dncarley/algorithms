
class BinaryNode:
    
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, root=None, data=None):
        if self.root == None:
            self.root = BinaryNode(data)
        else:
            if root is None:
                root = BinaryNode(data)
            elif data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def pre_order(self, root=None):
        if root:
            print(root.data)
            if root.left:
                self.pre_order(root.left)
            if root.right:
                self.pre_order(root.right)
            
binary_tree = BinaryTree()
binary_tree.insert(binary_tree.root, 1)
binary_tree.insert(binary_tree.root, 2)
binary_tree.insert(binary_tree.root, 3)
binary_tree.insert(binary_tree.root, 4)
binary_tree.insert(binary_tree.root, 4)
binary_tree.insert(binary_tree.root, 3)
binary_tree.insert(binary_tree.root, 4)
binary_tree.insert(binary_tree.root, -12)
binary_tree.insert(binary_tree.root, 'a')
binary_tree.insert(binary_tree.root, binary_tree)
binary_tree.insert(binary_tree.root, 2**256)
binary_tree.pre_order(binary_tree.root)


