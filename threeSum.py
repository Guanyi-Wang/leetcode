
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

print(threeSum(nums = [-1,0,1,2,-1,-4]))
