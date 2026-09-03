"""
As with all interval problems, we sort here using .sort().

We then could solve this using greedy?


"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        i = 0
        j = 1
        n = len(intervals)
        
        count = 0
        while j < n:

            if intervals[j][0] < intervals[i][1]: #if they overlap
                count += 1
                if intervals[j][1] < intervals[i][1]: #if the next interval's end time is less than the current interval's end time, then we doulr rather use the one with les end time, because then there is less room to overlap
                    i = j                            
            else:
                i = j #move onto the next intervals
            j += 1

        
        return count
        