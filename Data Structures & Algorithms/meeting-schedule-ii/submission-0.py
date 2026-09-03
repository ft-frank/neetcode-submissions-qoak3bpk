"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Rephrase the question.
What is the MINIMUM number of rooms required. Therefore we can look into a greedy algorithm here
What is the MAXIMUM number of events happening at the same time?


"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end,-1))
        
        time.sort(key = lambda x:(x[0], x[1])) #sort by start-time then end-time

        res = count = 0

        for t in time: #whenever an event starts, increase. whenever an event ends, decrease. In chronological order, so accurate at every time period.
            count += t[1]
            res = max(res, count)
        return res
        

        