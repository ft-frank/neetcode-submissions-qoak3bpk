# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""

Recursive Algorithm (previous, start)

1. Save first node
2. Iteratively reverse the k nodes
3. Stop if it doesn't reach to k nodes.
4. The previous.next should now point to the final ndoe that this iterative process iterated on, then pass on this final node to next recursive iteration


1->2->3->4->5->6


"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
        #where previous is the end node of the previous recursion
        # def recurse(previous, start):
        #     nonlocal k
        #     current = start
        #     i = 0
        #     while i < k and current is not None:
        #         next_temp = current.next
        #         current.next = prev
        #         prev = current
        #         current = next_temp
        #     if current is None:
        #         return
        #     else:
        #         recurse(current, current.next)

        current = head
        
        """
        Below algo produces
        3->2->1->NONE 6->5->4->None.
        At 
        1->2->3

        We save the 1.

        Then once we finish, since we haven't saved the 1 in another variable, we now officially save it.
        Then when we iterate 6->5->4, now that we have something saved, we assign start to the current, and then the new_start as the 4
        """
        prev_start = None
        dummy = None
        while current is not None: 
            i = 0
            prev = None
            start = current
            #I NEED TO SEE IF THE NEXT K NODES EXISTS
            while i < k and current: #Just looking at the next k elements to see if there are enough
                current = current.next
                i+=1
            current = start
            if i < k:
                prev_start.next = current
                return dummy
            else:
                i = 0
            # 3->2->1-> None
            while i < k and current is not None: #REVERSE
                next_temp = current.next 
                current.next = prev #4 points to None, just as 1 does
                prev = current
                current = next_temp
                i+=1
            #would end on prev being 3, and current being 4
            if not prev_start:
                prev_start = start #prev_start is now 1
            else: #prev_start is 1, so 1.next is prev, which should be 6
                prev_start.next = prev
                prev_start = start #prev_start now 4
            if not dummy:
                dummy = prev

        return dummy
        



"""
Now, if identify that k nodes aren't left, then i just attach current to 


"""
            

            





