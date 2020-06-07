from typing import List
"""
1. Compare interval to find the overlapped ones
2. merge them , keep it updated as newInterval
3. Since the intervals are sorted,  we know when to add the merged newInterval
4. Keep in mind the merged newInterval might be put in the end 
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        res = []
        def mergeTwo(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        for interval in intervals:
            if not newInterval or interval[1] < newInterval[0]:  # non-overlapped intervals on the left of newInterval or newInterval has been set
                res.append(interval)
            elif interval [0] > newInterval[1]: # first non-overlapped interval on the right of merged newInterval
                res.append(newInterval)
                res.append(interval)
                newInterval = []
            else:
                newInterval = mergeTwo(interval, newInterval)
        if  newInterval:  # In case the newInterval is the end
            res.append(newInterval)
        return res
