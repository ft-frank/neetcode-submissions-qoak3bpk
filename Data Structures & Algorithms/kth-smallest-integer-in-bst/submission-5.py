# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
We do a left side first, then node, then right side DFS

Once we have found the kth smallest value, by going towards the left, we append it, then the node, then the right side

"""



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            #If doesn't have anymore children
            dfs(node.left) #explore down left first
            if cnt == 0: #If the cnt already is 0, then w already have our res, return
                return
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)


        dfs(root)
        return res


        