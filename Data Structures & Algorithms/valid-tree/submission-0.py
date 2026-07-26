class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        """
        What is a valid tree?
        A tree is a graph with these two conditions

        1. A tree is is not cyclic. We can use topological sort to identify this.
        2. A tree has all connected edges. We can use an adjacency list to identify this

        As the edges are undirected, we cannot use topological sort concisely.
        
        We thus therefore use DFS. 
        DFS can identify cycles within the graph. 
        We use a visited set to track with nodes we have already visited.
        Then if we haven't visited all nodes by the end of DFS, we return False
        We return True,

        We keep track of the previous parent node that we just called, to avoid 
        going backwards. This means if we follow edges and end up back at the 
        parent node, then cycle, because parent node in cycle.

        A note for this is that it wasn't obvious that 0 was the parent?
    
        """

        visited = set()
        adjacency = {i: [] for i in range(n)}

        for e in edges:
            adjacency[e[0]].append(e[1])
            adjacency[e[1]].append(e[0])


        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nbr in adjacency[node]:
                #need to skip parent node
                if nbr == par:
                    continue
                if not dfs(nbr, node):
                    return False
            return True

            
        if dfs(0, -1) == False:
            return False

        if len(visited) != n:
            return False
        return True

        