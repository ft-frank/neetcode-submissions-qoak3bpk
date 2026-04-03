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
            if node is None:
                return True
            if minimum < node.val < maximum:
                return True and check(node.left, minimum, node.val) and check(node.right, node.val, maximum)
            else:
                return False
        minimum = float('-inf')
        maximum = float('inf')
        return check(root, minimum, maximum)
       