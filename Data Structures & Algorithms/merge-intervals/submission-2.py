"""
I have to sort the intervals.


"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        i = 0 #current interval
        j = 1 #nextInterval
        n = len(intervals)

        intervals.sort()


        res = []

        while j < n:
            newInterval = list(intervals[i])
            while j < n and intervals[j][0] <= newInterval[1]: 
                #while next interval has a start time that is less than or equal to the previous interval's end time
                newInterval[0] = min(newInterval[0], intervals[j][0])
                newInterval[1] = max(newInterval[1], intervals[j][1])
                j += 1
            res.append(newInterval)
            i = j
            j = i + 1
        while i < n:
            
            res.append(intervals[i])
            i += 1

        return res
            

                 


        