class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degrees = {i:0 for i in range(numCourses)}
        adjacency_list = {i:[] for i in range(numCourses)}

        for course, pre, in prerequisites:
            adjacency_list[course].append(pre)
            in_degrees[pre] += 1
        """
        By this point we have established a hashmap of indegrees, and a adjacency List
        for directional edges
        """

        
        topo_order = []

        degree_zero = [j for j in in_degrees if in_degrees[j] == 0]

        while degree_zero:

            course = degree_zero.pop()
            topo_order.append(course)
            for nbr in adjacency_list[course]:
                in_degrees[nbr] -= 1
                if in_degrees[nbr] == 0:
                    degree_zero.append(nbr)
        topo_order.reverse()
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []