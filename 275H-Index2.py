class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations or citations == [0]:
            return 0
        c_len = len(citations)
        left = 0
        right = c_len-1
        while left <= right:
            mid = (left+right)//2
            if citations[mid] == c_len -mid: # excactly N-h value less than h(mid)
                return citations[mid]
            if citations[mid] > c_len -mid:
                right = mid-1
            else:
                left = mid +1
        return c_len - left  # return maximum h