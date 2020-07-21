"""
O(k^2) Simple Heap solution
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k = min(len(nums1)*len(nums2), k)
        hp = [(n1+n2, n1, n2) for n1 in nums1[:k] for n2 in nums2[:k]]
        heapq.heapify(hp)
        res = []
        for _ in range(k):
            s, n1, n2 = heapq.heappop(hp)
            res.append([n1, n2])
        return res

"""
Store (sum, index1, index2) in a min heap.
if (sum, i, j) is popped, push (sum, i+1, j) and (sum, i, j+1)
since there are duplicates,  use a visited dict.
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return
        k = min(len(nums1)*len(nums2), k)
        hp = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0):1}
        res = []
        for _ in range(k):
            s, n1, n2 = heapq.heappop(hp)
            res.append([nums1[n1], nums2[n2]])
            if n1 +1 < len(nums1) and (n1 +1, n2) not in visited:
                heapq.heappush(hp, (nums1[n1+1]+nums2[n2], n1+1, n2))
                visited[(n1+1, n2)] = 1
            if n2 +1 < len(nums2) and  (n1, n2 +1) not in visited:
                heapq.heappush(hp, (nums1[n1]+nums2[n2+1], n1, n2+1))
                visited[(n1, n2+1)] = 1
            print(hp)

        return res