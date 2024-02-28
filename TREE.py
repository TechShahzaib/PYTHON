class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def LNR(self, node):
        if node is None:
            return
        self.LNR(node.left)
        print(node.data)
        self.LNR(node.right)
# Creating nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# Creating a binary tree
tree = BinaryTree()
tree.root = root
# In-order traversal
tree.LNR(tree.root) 


# # pre-order traversal
# tree.NLR(tree.root) 



# # post-order traversal
# tree.LRN(tree.root) 



































