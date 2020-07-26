class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = collections.Counter(nums)
        return [c  for c in counts if counts[c]>(len(nums)//3)]