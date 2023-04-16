class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start = ListNode(0)
        start.next = head
        dummy = start

        while start.next:
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next

        return dummy.next
