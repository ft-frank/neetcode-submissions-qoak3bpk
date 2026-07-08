# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root


        def search(node):
            if p.val < node.val and q.val < node.val:
                return search(node.left)
            elif p.val > node.val and q.val > node.val:
                return search(node.right)
            else:
                return node

        res = search(root)
        return res