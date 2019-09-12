class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # dynamic memory list to log the sum
        mem = [1, 10]
        if n >= 2:
            for i in range(2, n + 1):
                temp = 9
                for j in range(0, i - 1):
                    temp = temp * (9 - j)
                mem.append(temp + mem[i - 1])
        return mem[n]


