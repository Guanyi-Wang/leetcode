class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for i in range(1, n):
            count = 0
            val = result[0]
            temp = ''
            for s in result:
                if s == val:
                    count += 1
                else:
                    temp += str(count) + val
                    count = 1
                    val = s
            temp += str(count) + val
            result = temp
        return result
