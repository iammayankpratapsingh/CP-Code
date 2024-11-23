class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(root, left=float('-inf'), right=float('inf')):
    if not root:
        return True
    if root.val <= left or root.val >= right:
        return False
    return isBST(root.left, left, root.val) and isBST(root.right, root.val, right)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isBST(root))
