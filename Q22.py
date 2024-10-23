class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage:
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
head.next = second
second.next = third
third.next = second  # Create a cycle

print("Has Cycle:", has_cycle(head))
