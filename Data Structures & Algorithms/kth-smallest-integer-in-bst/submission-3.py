# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Optimal Sol right here!. I have to figure it out. Later.
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val if root else 0

        def dfs(node):
            nonlocal cnt
            nonlocal res
            if not node:
                return
            if node.left:
                dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            else:
                dfs(node.right)

        dfs(root)
        return res