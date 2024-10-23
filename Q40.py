class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    slow, fast = head, head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True

# Example usage:
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print("Is Palindrome:", is_palindrome(head))
