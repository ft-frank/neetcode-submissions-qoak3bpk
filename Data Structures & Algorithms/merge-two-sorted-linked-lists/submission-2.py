# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        l1 = list1
        l2 = list2
        while l1 and l2:

            if l1.val >= l2.val:
                current.next = l2
                l2 = l2.next
                
            elif l2.val > l1.val:
                current.next = l1
                l1 = l1.next
            current = current.next
        while l1:
            current.next = l1
            current = current.next
            l1 = l1.next
        while l2:
            current.next = l2
            current = current.next
            l2 = l2.next
                

        return dummy.next


