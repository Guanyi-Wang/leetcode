class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        keep aware of the positions of first one and two. Change values directly instead of         swap since only three nums. Two swaps for 0 and only one swao for 1.
        Do not return anything, modify nums in-place instead.
        """
        f1 = f2 = 0  # pointers at first one and two in the list
        for i in range(len(nums)):
            v = nums[i]
            nums[i] = 2  #  always swap to two
            if v < 2:  # do for 1 or 0
                nums[f2] = 1  # swap one to the beginning of twos
                f2 += 1
            if v == 0:  # only do for 0
                nums[f1] = 0  # swap zero to the begginning of ones
                f1 += 1