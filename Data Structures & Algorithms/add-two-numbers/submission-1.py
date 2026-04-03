# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = ListNode()
        current = dummy
        while cur1 or cur2:
            if cur1 is None:
                digit = cur2.val
            elif cur2 is None:
                digit = cur1.val
            else:
                digit = cur1.val + cur2.val
            digit += carry
            if digit >= 10:
                digit = digit - 10
                carry = 1
            else: 
                carry = 0
            
            newNode = ListNode(digit) 
            current.next = newNode
            current = current.next
            if cur1:
              cur1 = cur1.next
            if cur2:
              cur2 = cur2.next


        if carry > 0:
            extra = ListNode(1)
            current.next = extra

        
        
        
        return dummy.next