"""
Bucket
Put n elements in n-1 Buckets in between min(n) and max(n).
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_n = max(nums)
        min_n = min(nums)
        if max_n == min_n:
            return 0
        num_bucket = len(nums) - 1
        bucket_size = math.ceil((max_n - min_n) / num_bucket)
        bucket = [[None, None] for _ in range(num_bucket)]
        for n in nums:
            if n != max_n:
                i = (n - min_n) // bucket_size
                bucket[i][0] = n if not bucket[i][0] else min(bucket[i][0], n)  # min in bucket
                bucket[i][1] = n if not bucket[i][1] else max(bucket[i][1], n)  # max in bucket
        res = 0
        prev_max = bucket[0][1]
        for i in range(1, len(bucket)):
            if bucket[i][0]:
                res = max(res, bucket[i][0] - prev_max)
                prev_max = bucket[i][1]
        return max(res, max_n - prev_max)  # max_n might not in the buckets
