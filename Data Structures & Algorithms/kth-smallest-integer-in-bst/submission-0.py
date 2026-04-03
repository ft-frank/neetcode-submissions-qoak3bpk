# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_values = []
        def dfs(node):
            nonlocal ordered_values
            if node is None:
                return
            elif node.left is not None:
                dfs(node.left)
            ordered_values.append(node.val)
            dfs(node.right)
        dfs(root)
        return ordered_values[k - 1]