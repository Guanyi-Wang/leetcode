from typing import List

def threeSum( nums: [int]) -> [[int]]:
    solution = []
    # nums.sort()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    sol = [nums[i], nums[j], nums[k]]
                    sol.sort()
                    if sol not in solution:
                        solution.append(sol)
    return solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:  # sum of positive is positive
                break
            if i > 0 and nums[i] == nums[i - 1]:  # ignore duplicate
                continue
            l = i + 1
            r = len(nums) - 1
            two_sum = 0 - nums[i]
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
        return res
