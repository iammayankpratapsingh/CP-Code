class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

def get_middle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return mid

def sort_list(head):
    if not head or not head.next:
        return head
    mid = get_middle(head)
    left = sort_list(head)
    right = sort_list(mid)
    return merge_two_lists(left, right)

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Example usage:
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print("Original List:")
print_list(head)

sorted_head = sort_list(head)
print("Sorted List:")
print_list(sorted_head)
