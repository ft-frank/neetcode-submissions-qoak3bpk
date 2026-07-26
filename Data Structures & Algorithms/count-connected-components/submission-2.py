class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        """
        Run DFS, on a node. See whats not in visited yet.
        Run DFS on that, increment res by 1. Continue until
        all nodes visited.
        Return res


        """

        res = 0

        adjacency = {i:[] for i in range(n)}
        nodes_left = {j for j in range(n)}
        visited = set()

        for e in edges:
            adjacency[e[0]].append(e[1])
            adjacency[e[1]].append(e[0])
       

        def dfs(node): #explores all neighbours, adding to visited, until none left to visit.
            if node in visited:
                return
            visited.add(node)
            for nbr in adjacency[node]:
                dfs(nbr) 

        while len(visited) != n:
            res += 1
            nodes_left = nodes_left - visited
            nodes_left = list(nodes_left)
            dfs(nodes_left[0])
            nodes_left = set(nodes_left)

        return res

            # now I need to be able to run DFS on an unseen node
            #looks like the problem here is I can't just access a random element in a hashSest

            

        
            

        

