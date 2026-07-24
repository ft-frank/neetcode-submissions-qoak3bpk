"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        seen = set()
        created = {}

        def dfs(node):
            if node in seen:
                val = node.val
                return created[val] #return the new_node that has already been created
            if node is None:
                return
            seen.add(node)
            new_node = Node(node.val)
            created[new_node.val] = new_node
            for n in node.neighbors:
                nbr = dfs(n) #either returns already copied node, or creates aa new copy
                new_node.neighbors.append(nbr)
            return new_node
        return dfs(node)