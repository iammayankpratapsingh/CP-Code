class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev, current = dummy, head
    while current and current.next:
        next_pair = current.next.next
        second = current.next
        second.next = current
        current.next = next_pair
        prev.next = second
        prev = current
        current = next_pair
    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Original List:")
print_list(head)
swapped_list = swap_pairs(head)
print("Swapped in Pairs:")
print_list(swapped_list)
