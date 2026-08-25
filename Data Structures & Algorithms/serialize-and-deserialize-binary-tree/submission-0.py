# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Deserialise can use a DFS algorithm, pre-order traversal.

1, 2, null, null, 3, 4, null, null, 5, null, null

To deserialise Use dfs.


To deal with multidigit values, we use #. 

Like to deserialise.

1#2#n#n#33#44#




"""

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if node is None:
                res.append('n#')
                return
            res.append(str(node.val))
            res.append('#')

            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        res = "".join(res)

        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        index = 0

        def dfs(node = None):
            nonlocal index
            val, index = self.readValue(index, data)
            if val is None:
                return None
            new_node = TreeNode(val)
            new_node.left = dfs()
            new_node.right = dfs()
        

            return new_node


        return dfs()

    def readValue(self, index, data):
        val = []
        if index >= len(data):
            return (None, index)
        if data[index] == 'n':
            index += 2
            return (None, index)

        while data[index] != '#':
            val.append(data[index])
            index += 1
        val = int("".join(val))
        index += 1 #move onto the next integer
        
        return (val, index)

            


