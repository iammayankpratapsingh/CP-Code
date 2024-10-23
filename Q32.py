class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    # Step 1: Create new nodes and interweave them with original nodes
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    # Step 2: Assign random pointers for the new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate the new nodes to form the new list
    old_list = head
    new_list = head.next
    new_head = head.next
    while old_list:
        old_list.next = old_list.next.next
        if new_list.next:
            new_list.next = new_list.next.next
        old_list = old_list.next
        new_list = new_list.next
    
    return new_head

# Example usage:
head = Node(1, Node(2, Node(3)))
head.random = head.next.next
head.next.random = head

cloned_list = copy_random_list(head)
# We can't easily print random pointers, but the list is cloned.
print("Cloned list created successfully.")
