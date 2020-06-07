class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        We can infer the exact location of each num in list since it's sorted, by keeping one pointer points on the end of non-duplicates part.
        """
        if len(nums) < 3:
            return len(nums)
        i = 2  # first two will always fit
        for n in nums[2:]:
            # three cases: 1. n<nums[i-2] not exist since sorted.2.n==nums[i-2], two same nums already exist. 3. n >
            # nums[i-2], introduce new num
            if n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            """
            Very straight forward solution. Just count each num's apparence, and return the number of unique num.
            """
            if len(nums) < 3:
                return len(nums)
            res = 1
            count = 1
            for i in range(1, len(nums)):
                if nums[i - 1] == nums[i]:
                    count += 1
                    if count > 2:
                        continue
                else:
                    count = 1
                nums[res] = nums[i]
                res += 1
            return res