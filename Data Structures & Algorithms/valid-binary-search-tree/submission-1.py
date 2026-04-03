# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def check(node, minimum, maximum):
            res = True
            if node is None:
                return res
            if node.val < maximum  and node.val > minimum:
                return res and check(node.left, minimum, min(maximum, node.val)) and check(node.right, max(minimum, node.val), maximum)
            else:
                return False
        minimum = float('-inf')
        maximum = float('inf')
        return check(root, minimum, maximum)
       