class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    before_head = ListNode(0)
    after_head = ListNode(0)
    before = before_head
    after = after_head
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print("Original List:")
print_list(head)
partitioned_list = partition(head, 3)
print("Partitioned List:")
print_list(partitioned_list)
