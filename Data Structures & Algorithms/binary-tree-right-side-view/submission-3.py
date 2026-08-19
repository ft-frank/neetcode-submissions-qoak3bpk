# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
BFS algorithm where I add the value of the node at the end of a BFS run to res

"""
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []    


        search = deque([root])
        

        while search:
            temp = deque([])
            #I have to append the value of the right most node in search to res.
            if search and search[-1]:
                res.append(search[-1].val)
            for _ in range(len(search)):
                node = search.popleft()
                if not node:
                    return []
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right) 

            search = temp

            #Then search becomes temp, and temp gets reset
                       
        return res

        
        