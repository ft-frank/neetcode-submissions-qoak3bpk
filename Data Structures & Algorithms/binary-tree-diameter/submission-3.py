# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            if node is None:
                return -1
            nonlocal diameter

            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            diameter = max(diameter, left + right)
            return max(left, right)

        dfs(root)
        return diameter