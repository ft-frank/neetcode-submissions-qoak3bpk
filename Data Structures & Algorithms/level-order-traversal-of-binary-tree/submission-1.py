# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        roots = [[root]] if root else []
        res = [[root.val]] if root else []
        def bfs():
            nonlocal roots
            sublist = []
            vals = []
            if len(roots) > 0:
                for node in roots[-1]:
                    if node.left: 
                        sublist.append(node.left)
                        vals.append(node.left.val)
                    if node.right:
                        sublist.append(node.right)
                        vals.append(node.right.val)
            if len(sublist) > 0:
                res.append(vals)
                roots.append(sublist)
                bfs()
            return 
        bfs()
        return res

