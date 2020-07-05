class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        for i, j in tickets:
            dic[i].append(j)
        for key in dic:
            dic[key].sort(reverse=True)  # dec order to pop min
        print(dic)
        stack = ['JFK']
        res = []
        while stack:
            while dic[stack[-1]]:
                stack.append(dic[stack[-1]].pop())
            else:
                # This airport should be the last to go since we can't go anywhere from here.
                res.append(stack.pop())
        return res[::-1]


