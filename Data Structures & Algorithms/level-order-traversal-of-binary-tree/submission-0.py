# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if root is None:
            return res
        row = [root] 
        res.append([root.val])

        while len(row) > 0: 
            sublist = []
            next_row = []
            for node in row:
                if node.left is not None:
                    sublist.append(node.left.val)
                    next_row.append(node.left)
                if node.right is not None:
                    sublist.append(node.right.val)
                    next_row.append(node.right)
            
            row = next_row
            if len(row) > 0:
                res.append(sublist)
        return res

                
            