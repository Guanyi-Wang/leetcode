from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        1.sort intervals based on their start index
        2.merge the overlapped intervals one by one
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in intervals:
            if merged[-1][1] < i[0]:
                merged.append(i)
            else:  # overlapped
                merged[-1][1] = max(i[1], merged[-1][1])  # start is sorted not end, so we use max to find end index
        return merged