# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def check(p, q):
            nonlocal res
            if p is None and q is None:
                return
            elif p is None or q is None:
                res = False
                return
            elif p.val != q.val:
                res = False
            check(p.left, q.left)
            check(p.right, q.right)

        check(p, q)
        return res

            