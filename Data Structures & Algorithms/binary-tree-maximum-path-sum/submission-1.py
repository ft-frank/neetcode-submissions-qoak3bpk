# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
For each node, the maximum if that node were the root is
node.val + dfs(node.left) + dfs(node.right)



"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val



        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            res = max(res, node.val + left + right)

            return max(node.val + left, node.val + right, 0)

            
        dfs(root)
        return res


