class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [key for key, value in collections.Counter(nums).items() if value==2]