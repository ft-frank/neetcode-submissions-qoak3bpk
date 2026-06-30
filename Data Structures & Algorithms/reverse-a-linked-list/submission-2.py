# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev_pointer = None
        while current is not None:
            next_pointer = current.next
            current.next = prev_pointer
            prev_pointer = current
            current = next_pointer
        return prev_pointer
