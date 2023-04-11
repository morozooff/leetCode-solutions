# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        pointer = head
        while pointer:
            while pointer.next and pointer.next.val == pointer.val:
                pointer.next = pointer.next.next
            pointer = pointer.next
        return head