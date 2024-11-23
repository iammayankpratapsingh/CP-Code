class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printPaths(root, path=[]):
    if not root:
        return
    path.append(root.val)
    if not root.left and not root.right:
        print(path)
    else:
        printPaths(root.left, path.copy())
        printPaths(root.right, path.copy())

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

printPaths(root)
