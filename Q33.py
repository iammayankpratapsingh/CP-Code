class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_right(head, k):
    if not head:
        return head
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    k = k % length
    if k == 0:
        return head
    tail.next = head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original List:")
print_list(head)
rotated_list = rotate_right(head, 2)
print("Rotated List:")
print_list(rotated_list)
