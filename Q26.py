class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print("Sum of numbers represented by linked lists:")
result = add_two_numbers(l1, l2)
print_list(result)
