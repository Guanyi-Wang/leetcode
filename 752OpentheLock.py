import collections
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        des = {i: 1 for i in deadends}  # for time complexity
        seen = {}
        dq = collections.deque(['0000'])
        step = 0
        # bfs
        while dq:
            size = len(dq)
            for i in range(size):
                # print(dq)
                s = dq.popleft()
                if s in des or s in seen:  # deadends or seen before
                    continue  # skip this state
                if s == target:
                    return step
                seen[s] = 1
                states = []
                for i in range(len(s)):
                    if int(s[i]) < 9:
                        states.append(s[:i] + str(int(s[i]) + 1) + s[i + 1:])
                    if int(s[i]) > 0:
                        states.append(s[:i] + str(int(s[i]) - 1) + s[i + 1:])
                    if s[i] == '0':
                        states.append(s[:i] + '9' + s[i + 1:])
                    if s[i] == '9':
                        states.append(s[:i] + '0' + s[i + 1:])
                dq.extend(states)

            step += 1

        return -1