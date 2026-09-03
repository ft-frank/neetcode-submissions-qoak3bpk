"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #I have to sort it somehow by start_time
        list_of_intervals = []
        for interval_obj in intervals:
            new_interval = [interval_obj.start, interval_obj.end]
            list_of_intervals.append(new_interval)

        list_of_intervals.sort()
        i = 0
        n = len(list_of_intervals)
        while i < n-1:
            current = list_of_intervals[i]
            nxt = list_of_intervals[i + 1]
            if nxt[0] < current[1]:
                return False
            i += 1

        return True