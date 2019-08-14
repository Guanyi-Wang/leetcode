from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return None
##########################################################
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            tar = target - numbers[i]
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tar:
                    return [i + 1, mid + 1]
                if numbers[mid] > tar:
                    r = mid - 1
                else:
                    l = mid + 1
        return None
