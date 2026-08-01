# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Breadth first search until you find p or q. T
Then dfs from the found node, to be able to see if the other node is below it. If so, return the found node. 
Otherwise, return the ancestor of the breadth first search

"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val: #now we know p is always the lesser one. 
            q, p = p, q
        if not root:
            return root
        def search(node):
            if p.val <= node.val <= q.val:
                return node
            elif q.val < node.val:
                return search(node.left)
            else:
                return search(node.right)

        return search(root)