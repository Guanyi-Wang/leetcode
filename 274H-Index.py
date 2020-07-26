class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        c_len = len(citations)
        for i in range(c_len):
            if c_len - i  <= citations[i]:
                return c_len - i
        return 0