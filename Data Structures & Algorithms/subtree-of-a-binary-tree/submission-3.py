# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        current_search = True

        def dfs(root):
            nonlocal res
            nonlocal current_search
            if not root:
                return
            if root.val == subRoot.val:
                match(root, subRoot)
                if current_search == True:
                    res = True
                current_search = True
            dfs(root.left)
            dfs(root.right)   

        def match(n1, n2):
            nonlocal current_search

            if n1 is None and n2 is None:
                return
            elif n1 and n2:
                if n1.val == n2.val:
                    match(n1.left, n2.left)
                    match(n1.right, n2.right)
                else:
                    current_search = False
            else:
                current_search = False

        dfs(root)
        return res
                