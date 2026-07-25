"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        link = {}

        
        def copy(node):
            if node is None:
                return
            
            if node.val in link:
                return link[node.val]
            
            copy_node = Node(node.val)
            link[node.val] = copy_node

            for nbr in node.neighbors:
                copy_node.neighbors.append(copy(nbr))
            
            return copy_node

        return copy(node)
            
        
