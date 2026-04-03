# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        current_row = [root]
        while len(current_row) > 0:
            res.append(current_row[-1].val)
            next_row = []
            for node in current_row:
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)    
            current_row = next_row

        return res

