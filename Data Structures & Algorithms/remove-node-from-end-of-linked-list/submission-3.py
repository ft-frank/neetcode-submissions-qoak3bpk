# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        prev = None
        current.prev = prev

        while current: #turn into a double linked listS
            prev = current
            current = current.next
            if current:
                current.prev = prev
        #now prev is the last element
        current = prev

        for i in range(n - 1):
            current = current.prev

        
        if current.prev == None:
            return current.next
        else:
            nex = current.next
            current.prev.next = nex
            return head