class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    if not head:
        return head
    seen = set()
    current = head
    seen.add(current.val)
    while current and current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next
    return head

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
head = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(4))))))
print("Original List:")
print_list(head)
new_head = remove_duplicates(head)
print("List after removing duplicates:")
print_list(new_head)
