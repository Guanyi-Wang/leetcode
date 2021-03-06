class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        # stack stores tuple(value, minimum value at this moment)
        if not self.stack:
            self.stack.append((x,x))
        else:
            # compare this value with previous minimum value
            self.stack.append((x,min(self.stack[-1][1], x)))

    def pop(self) -> None:
        if not self.stack:
            return None
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()