# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
For these Tree problems and graph problems, recursion is ALWAYS optimal. Why the flap am I trying to do iterative.

And they either use DFS or BFS. Not really any other method here.

We identify DFS because it has two types, inorder and preorder, which is literally what they give us.

DFS optimal.


"""




class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preIdx = inIdx = 0
        def dfs(limit): #One of my first thinkings, should have looked at it closer

            nonlocal preIdx, inIdx

            if preIdx >= len(preorder):
                return None

            elif inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root


        return dfs(float('inf'))


