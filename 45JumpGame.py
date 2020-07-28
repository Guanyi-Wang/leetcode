"""
Backward Dynamic programming
Time Limit Exceeded
O(N^2)

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i]> len(nums)-2-i:
                nums[i] = 1
            else:
                min_step = len(nums)
                for j in range(i+1, i+nums[i]+1):
                    if j <=len(nums)-2:
                        min_step = min(min_step, nums[j])
                        if min_step == 1:
                            break
                nums[i] = min_step+1
        return nums[0]

"""
Greedy Solution.O(N)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        index =  0  # current reached index
        step = 0  # min steps taken to current index
        cur_Max = 0 # max index can be reached in this step
        next_Max  = 0 # max index can be reached in next step
        while cur_Max < len(nums)-1:
            while index <= cur_Max: # while index still in range of max of this step
                next_Max = max(next_Max, nums[index]+index) #update the max index of next step
                index += 1
            cur_Max = next_Max  # move a step forward and update current max index
            step+=1
        return step