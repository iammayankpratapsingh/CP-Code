class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# Example usage:
intersection = ListNode(8, ListNode(10))
listA = ListNode(4, ListNode(1, intersection))
listB = ListNode(5, ListNode(6, ListNode(1, intersection)))

print("Intersection at node with value:", get_intersection_node(listA, listB).val)
