class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_to_doubly_list(root):
    if not root:
        return None
    
    def convert(node):
        nonlocal first, last
        if node:
            convert(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            convert(node.right)

    first, last = None, None
    convert(root)
    return first

def print_doubly_list(node):
    while node:
        print(node.val, end=" <-> " if node.right else "")
        node = node.right
    print()

# Example usage:
root = Node(4, Node(2, Node(1), Node(3)), Node(5))
head = bst_to_doubly_list(root)
print("Doubly Linked List:")
print_doubly_list(head)
