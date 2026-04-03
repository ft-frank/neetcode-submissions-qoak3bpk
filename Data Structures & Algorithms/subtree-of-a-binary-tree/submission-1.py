# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def findRootEquality(root):
            nonlocal res
            if root.val == subRoot.val:
                res = res or check(root, subRoot)
            if root.left:
                findRootEquality(root.left)
            if root.right:
                findRootEquality(root.right)
        def check(root, subRoot): #check if there really is subRoot within root\
            if root is None and subRoot is None:
                return  True
            # elif subRoot is None and root is not None:
            #     return True
            elif root is None or subRoot is None:
                return False
            elif root.val != subRoot.val:
                return False
            else:
                return check(root.left, subRoot.left) and check(root.right, subRoot.right)
            
            
            
        findRootEquality(root)    
        return res