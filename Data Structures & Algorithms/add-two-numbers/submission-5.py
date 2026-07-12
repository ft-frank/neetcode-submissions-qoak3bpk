# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        head = l1
        while l1 and l2:    
            l1.val = l1.val + l2.val
            l1.val += carry
            if l1.val >= 10:
                l1.val -= 10
                carry = 1
            else:
                carry = 0
            prev = l1
            l1 = l1.next
            l2= l2.next
        if l2:
            prev.next = l2
            l1 = l2
        while l1:
            l1.val += carry
            if l1.val >= 10:
                l1.val -= 10
                carry = 1
            else:
                carry = 0
            prev = l1
            l1 = l1.next
        if carry > 0:
            l1 = prev
            l1.next = ListNode(1)
            
            
        return head