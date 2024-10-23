class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print("Merged List:")
merged_list = merge_two_lists(l1, l2)
print_list(merged_list)
