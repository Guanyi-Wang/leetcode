"""
Arrage task according to its frequence.
eg1:
2A 3B 3C 6D N=5
D B C A I I
D B C A I I
D B C I I I
D I I I I I
D I I I I I
D
eg2:
res = (max_count-1)*(N+1)+num_max_count = 5*6+1 = 31
2A 5B 3C 6D 3F N=2
D B C
D B C
D B C
D B F
D B F
D A F
A
res = len(tasks)

res = max(eg1, eg2)
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(collections.Counter(tasks).values())
        max_count = max(counts)
        n_max_count = counts.count(max_count)
        return max((max_count - 1) * (n + 1) + n_max_count, len(tasks))

