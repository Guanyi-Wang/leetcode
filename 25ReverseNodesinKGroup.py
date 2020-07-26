# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
In order to reverse k elements, insert 2nd to kth element into the front one by one.
[1,2,3,4]
[2,1,3,4]
[3,2,1,4]
[4,3,2,1]
dummy->  1  ->  2  ->  3  ->  4  ->  5  -> ...->None
prev   first   second        kth    last
"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if k == 1:
            return head
        # define previous element of first element
        prev = dummy = ListNode(0, head)
        while prev:
            # find the kth element after first and the next element of it
            last = prev
            for _ in range(k):
                if not last.next:
                    return dummy.next
                else:
                    last = last.next
            last = last.next

            # print('last is :{}'.format(last))
            # function to reverse list
            def reverse(prev, k):
                tail = prev.next  # first will become tail after reverse
                for _ in range(k - 1):
                    first = prev.next
                    second = tail.next
                    prev.next = second
                    tail.next = second.next
                    second.next = first
                return tail

            # reverse list and move forward
            prev = reverse(prev, k)
            # print('prev is:{}'.format(prev))
        return dummy.next
