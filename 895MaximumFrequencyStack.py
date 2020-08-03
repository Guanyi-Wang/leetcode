class FreqStack:

    def __init__(self):
        self.counts = collections.defaultdict(int)
        self.stack = []
        self.index = 0

    def push(self, x: int) -> None:
        self.counts[x] += 1
        heapq.heappush(self.stack, (-self.counts[x], -self.index, x))
        self.index += 1

    def pop(self) -> int:
        n = heapq.heappop(self.stack)
        self.counts[n[2]] -= 1
        return n[2]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()