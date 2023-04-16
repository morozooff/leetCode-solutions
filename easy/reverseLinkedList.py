# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        lst = []
        dummy = tail = head

        while head:
            lst.append(head.val)
            head = head.next

        while lst:
            tail.val = lst.pop()
            tail = tail.next

        return dummy