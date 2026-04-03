# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower = min(p.val, q.val)
        higher = max(p.val, q.val)
        def find(root):
            if root is None:
                return None
            if lower <= root.val and higher >= root.val:
                return root
            elif lower < root.val and higher < root.val:
                return find(root.left)
            else:
                return find(root.right)
        return find(root)



        