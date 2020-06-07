from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            three_sum = target - nums[i]
            res_three_sum = self.threeSum(nums[i + 1:], three_sum)
            if res_three_sum:
                for re in res_three_sum:
                    res.append([nums[i]] + re)
        return res

    def threeSum(self, nums: List[int], target) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # ignore duplicate
                continue
            l = i + 1
            r = len(nums) - 1
            two_sum = target - nums[i]
            while l < r:
                if nums[l] + nums[r] > two_sum:
                    r -= 1
                elif nums[l] + nums[r] < two_sum:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[r - 1] == nums[r]:  # ignore duplicate
                        r -= 1
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    # never forget to move pointers in normal cases
                    r -= 1
                    l += 1
