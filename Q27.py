class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return head
    pseudo_head = Node(0, None, head, None)
    prev = pseudo_head
    stack = [head]
    while stack:
        curr = stack.pop()
        prev.next = curr
        curr.prev = prev
        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr
    pseudo_head.next.prev = None
    return pseudo_head.next

def print_doubly_list(node):
    while node:
        print(node.val, end=" <-> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = Node(1, None, Node(2, None, Node(3, None, Node(4, None, None))))
head.child = Node(5, None, Node(6))
print("Flattened list:")
flattened_head = flatten(head)
print_doubly_list(flattened_head)
