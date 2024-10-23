class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    old_to_new = {}
    current = head
    while current:
        old_to_new[current] = Node(current.val)
        current = current.next
    current = head
    while current:
        old_to_new[current].next = old_to_new.get(current.next)
        old_to_new[current].random = old_to_new.get(current.random)
        current = current.next
    return old_to_new[head]

def print_random_list(head):
    current = head
    while current:
        rand_val = current.random.val if current.random else None
        print(f"Node({current.val}), Random({rand_val})", end=" -> ")
        current = current.next
    print()

# Example usage:
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
n1.random = n3
n2.random = n1

print("Original List:")
print_random_list(n1)

copied = copy_random_list(n1)
print("Copied List:")
print_random_list(copied)
