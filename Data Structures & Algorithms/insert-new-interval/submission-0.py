"""
So we are given the start time and end time of an interval. And we 
have to include that interval within the intervals list
such that the intervals items remain non-overlapping, and it laps over the interval we are given.




"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]: #look for first relevant interval
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        res.append(newInterval)


        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res



            

        