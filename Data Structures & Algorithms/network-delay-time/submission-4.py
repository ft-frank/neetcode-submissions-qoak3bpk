"""
We create an adjacency list, that shows which nodes connect to which nodes where finding that list
is O(1). 
Then starting at the node specified, we add each path to loading.
Loading is where when the time increments to the time specified, the path is taken, 
and then all paths will be added to loading.
We want to sort loading by the one with the minimum time necessary, therefore we can 
use a min-heap that auto adjusts.
Then once all nodes have been visited (tracked using a counter), we return the time needed.
However if loading becomes empty and we still haven't visisted all nodes, we return -1. 
This is therefore a BFS algorithm.

Instead of incrementing through t (as I have done mistakenly in other questions), instead push t up to the 
smallest relevant point for increased time efficiency

"""
from heapq import heappush, heappop, heapify

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        loading = []
        t = 0
        #adjacency list

        graph = [[] for _ in range(n)]
        for ui, vi, ti in times: #adjacency list created
            graph[ui-1].append((ti, vi)) #sort by ti first. The index is the key of the node - 1.

        for ti, vi in graph[k - 1]:
            heappush(loading, (ti + t, vi)) #t + ti, is when the time the signal reaches that node
        visited = set()
        visited.add(k)

        while loading and len(visited) < n:
            item = heappop(loading)
            if item[1] in visited: #we don't want to add a destiation node ot our loading, bcus already in it
                continue
            t = item[0]
            visited.add(item[1]) #we add all destination nodes to our visited, before we 'visit' them.
            for ti, vi in graph[item[1] - 1]:
                if vi not in visited:
                    heappush(loading, (ti + t, vi))


        return t if len(visited) == n else -1
        










        



