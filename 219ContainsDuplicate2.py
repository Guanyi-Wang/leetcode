class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or not k:
            return False
        dict = {}
        for i, n in enumerate(nums):
            if n in dict and i-dict[n]<=k:
                return True
            dict[n] = i
        return False