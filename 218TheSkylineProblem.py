"""
Generate two tuples based on start or end of building representing two events
start:(left, -height, right)
end: (right, 0, 0)
sort list[starts + ends] based on first and second key
iterate through list of events:
    pop low skylines already passed
    store (-height, right) in heap when meet a start event
    check if the height on the top heap same as the last appended in the result

heap keeps the min -height always on the top. and pop push only takes O(logn)

"""


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # build event list
        start = [(l, -neg_h, r) for l, r, neg_h in buildings]
        end = [(r, 0, 0) for _, r, _ in buildings]
        events = sorted(start + end)
        # initialize heap, result list
        hp = [(0, float('inf'))]
        res = [[0, 0]]
        for l, neg_h, r in events:
            # pop lower skylines already passed
            while l >= hp[0][1]:
                heapq.heappop(hp)
            # store height from start event
            if neg_h:
                heapq.heappush(hp, (neg_h, r))  # keep track of r--end point
            if res[-1][1] != -hp[0][0]:
                res.append([l, -hp[0][0]])
        return res[1:]
