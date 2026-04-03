# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        
        #forms doubly linked list

        prev = None
        while current.next:
            current.prev = prev
            prev = current
            current = current.next
        current.prev = prev

        for i in range(n - 1):
            current = current.prev

        #now on the one we should remove

        if current.prev and current.next:
            prev = current.prev
            nex = current.next
            prev.next = nex
        elif current.next is None and current.prev is None:
            head = None
        elif current.next is None:
            prev = current.prev
            prev.next = None
        elif current.prev is None:
            head = current.next
        return head


                