# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        if head.next is not None:
            fast = head.next
        else: 
            return False
        if fast.next is not None:
            fast = fast.next

        while fast.next is not None:
            if fast == slow:
                return True
            fast = fast.next
            if fast.next == None:
                return False
            else:
                fast = fast.next
            slow = slow.next

        return False