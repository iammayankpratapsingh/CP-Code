class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
inverted_root = invertTree(root)
print(inverted_root.val)
print(inverted_root.left.val) 
print(inverted_root.right.val)
