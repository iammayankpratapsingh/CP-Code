class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    def helper(node):
        if not node:
            return 0
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)
        max_sum[0] = max(max_sum[0], left + right + node.val)
        return node.val + max(left, right)
    
    max_sum = [float('-inf')]
    helper(root)
    return max_sum[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(maxPathSum(root))
