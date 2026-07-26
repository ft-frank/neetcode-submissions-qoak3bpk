"""
Topological Sort.

Can use Khan's algorithm or DFS. 

For prerequisites [[0, 1]], 
where 0 depends on 1.


"""



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        V = numCourses
        into_adjacency = {i: [] for i in range(V)} #this is how we can access neigbours
        in_degrees = {i:0 for i in range(V)}

        for course, pre in prerequisites:
            into_adjacency[course].append(pre) #create neigbhour List
            in_degrees[pre] += 1
        degree_zero = [j for j in in_degrees if in_degrees[j] == 0]
        topo_order = []

        while degree_zero:
            course = degree_zero.pop() #a course number
            topo_order.append(course) #add course number to list, because it has no pres needed

            for nbr in into_adjacency[course]:
                in_degrees[nbr] -= 1
                if in_degrees[nbr] == 0:
                    degree_zero.append(nbr)


        if len(topo_order) < V:
            return False
        return True


            

       
     


