# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
N nums in total in K lists
Build a heap to store the first one element in each list.O(k)
Pop(O(logk)) the min element in the heap and then push(O(logK)) min.next into heap.
Use the popped element to build the linked list.
Worth mention that instead of storing node in heap, we store tuple (node.val, i, node), node.val as prority key, i is the ith list in k lists, use this to avoid comparing node when node.val is same.
eg. comparing (1, node), (1, node) will raise an error but introducing i will never make the algorithm compare node.
Time complexity: O(k+N(2log(k))+N) = O(Nlog(K))
"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        res = ListNode()
        cur = res
        while heap:
            v, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return res.next
