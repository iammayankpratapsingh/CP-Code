class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original List:")
print_list(head)
new_head = remove_nth_from_end(head, 2)
print("List after removing 2nd node from end:")
print_list(new_head)
