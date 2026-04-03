# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            next_temp = current.next  # Save this FIRST!
            current.next = prev       # Reverse the pointer
            prev = current           # Move prev forward
            current = next_temp      # Move current forward using saved value
        return prev


        