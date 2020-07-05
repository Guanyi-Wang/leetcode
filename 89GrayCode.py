from typing import List
"""
eg. n = 3
if we know the solution for n=2
0 --- 00                            0 --- 000
2 --- 10   add 0 to the first =>    2 --- 010
3 --- 11                            3 --- 011
1 --- 01                            1 --- 001

then change first digit from 0 to 1
0 --- 000                          0 --- 000 
2 --- 010                          2 --- 010
3 --- 011                          3 --- 011
1 --- 001                          1 --- 001
=========                          =========  
4 --- 100                          5 --- 101  5 = 1+2^(3-1)=1+1<<3-1
6 --- 110  => reverse this part    7 --- 111  7 = 3+2^(3-1)
7 --- 111                          6 --- 110  6 = 2+2^(3-1)
5 --- 101                          4 --- 100  4 = 1+2^(3-1)
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if not n:
            return [0]
        gc = [0]
        for i in range(1,n+1):
            temp = gc[::-1]
            for j in range(len(temp)):
                temp[j] += 1<< i-1
            gc += temp
        return gc