# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, prev_highest):
            nonlocal res
            if node.val >= prev_highest:
                res += 1
                prev_highest = node.val
            if node.left:
                dfs(node.left, prev_highest)
            if node.right:
                dfs(node.right, prev_highest)
        dfs(root, -101)
        return res
        
