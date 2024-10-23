class Node:
    def __init__(self, val, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return None
    stack = []
    current = head
    while current:
        if current.child:
            if current.next:
                stack.append(current.next)
            current.next = current.child
            current.child = None
        if not current.next and stack:
            current.next = stack.pop()
        current = current.next
    return head

def print_flatten_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = Node(1, Node(2, Node(3, None, Node(7, Node(8)))))
flattened_list = flatten(head)
print("Flattened List:")
print_flatten_list(flattened_list)
