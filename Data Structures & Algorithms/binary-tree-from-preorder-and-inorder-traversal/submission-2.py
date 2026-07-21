# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx

            if preIdx >= len(preorder): #already created all the nodes possible
                return None
            
            if  inorder[inIdx] == limit: #the 
                inIdx += 1
                return None

            newNode = TreeNode(preorder[preIdx])
            preIdx += 1
            newNode.left = dfs(newNode.val) #create a left if current inOrder is not 1, that means its still on left
            newNode.right = dfs(limit) #create right unless conditions two conditions above

            return newNode

        return dfs(float('inf'))