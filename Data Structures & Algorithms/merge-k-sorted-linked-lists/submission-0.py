# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""



1. Merge l0 and l1 to create l1. Merge l1 and l2. etc.
2. Merge l0 and l1, l1 and l2 at the same time. Like in merge sort.

Second method can be done iteratively or recursively.
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        def combine(nodeList):

            if len(nodeList) == 0:
                return None

            if len(nodeList) == 1:
                return nodeList[0]

            elif len(nodeList) == 2:
                new = merge(nodeList[0], nodeList[1])
                return new

            n = len(nodeList)
            mid = n // 2
            leftList = combine(nodeList[:mid]) #This is the part I am messing up here
            rightList = combine(nodeList[mid:])

            combined = merge(leftList, rightList)
            return combined
        

        def merge(l1, l2): #the algo that merges two linked lists. Pretty standard formula that I should be able to figure out.....

            head = ListNode()
            current = head

            while l1 and l2:

                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next            

            while l1:
                current.next = l1
                current = current.next
                l1 = l1.next    
            
            while l2:
                current.next = l2
                current = current.next
                l2 = l2.next  

            return head.next



        return combine(lists)