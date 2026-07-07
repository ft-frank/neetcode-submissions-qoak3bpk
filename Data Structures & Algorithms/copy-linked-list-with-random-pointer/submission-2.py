"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen_random = {None:None}

        current = head
        prev = None
        new_head = None
        while current:
            new = Node(current.val)
            if prev:
                prev.next = new
            else:
                new_head = new
            seen_random[current] = new
            prev = new
            current = current.next

        current = head

        while current:
            seen_random[current].random = seen_random[current.random]
            current = current.next


      #above generates the new list with the values, but now I need the values.
        return new_head