class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    # Function to reverse the nodes from start to end
    def reverse(start, end):
        prev, current = None, start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    # Dummy node initialization to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
    
    while True:
        kth = group_prev
        # Find the kth node
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        
        group_next = kth.next
        # Reverse the group
        prev, curr = group_prev.next, group_prev.next
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
        group_prev.next = group_next

    return dummy.next

# Helper function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
print("Original List:")
print_list(head)
reversed_list = reverse_k_group(head, k)
print(f"Reversed in groups of {k}:")
print_list(reversed_list)
