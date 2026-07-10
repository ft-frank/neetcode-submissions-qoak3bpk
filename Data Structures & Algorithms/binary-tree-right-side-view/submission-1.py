# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = [root] if root else []
        vals = []

        while len(nodes) > 0:
            next_breadth = []
            vals.append(nodes[-1].val)
            for node in nodes:
                if node.left:
                    next_breadth.append(node.left)
                if node.right:
                    next_breadth.append(node.right)
            nodes = next_breadth



        return vals