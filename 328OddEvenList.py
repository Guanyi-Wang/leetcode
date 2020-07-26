# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
h  ->  1  ->  2  ->  3  ->  4  ->  5  ->  None
      odd
      cur
      count = 1%2 ==1
    cur = cur.next
    count +=1
h  ->  1  ->  2  ->  3  ->  4  ->  5  ->  None
      odd
             cur    next_odd
             count=2
    next_odd = cur.next
    cur.next = next_odd.next
    next_odd.next = odd.next
    odd.next = next_odd
    odd = odd.next
    count+=1

h  ->  1  ->  3  -> 2  ->  4  ->  5  ->  None
      odd
                   cur
    odd = odd.next
    count+=1
h  ->  1  ->  3  -> 2  ->  4  ->  5  ->  None
            odd
                   cur
                   count = 3
h  ->  1  ->  3  -> 2  ->  4  ->  5  ->  None
            odd
                          cur    next_odd
                          count = 4
            next_odd = cur.next
            cur.next = next_odd.next
            next_odd.next = odd.next
            odd.next = next_odd
            odd = odd.next
            count+=1
"""


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = cur = head
        count = 1
        while cur:
            if count % 2:
                cur = cur.next
                count += 1
            elif cur.next:  # in case list is even length
                next_odd = cur.next
                cur.next = next_odd.next
                next_odd.next = odd.next
                odd.next = next_odd
                odd = odd.next
                count += 1
            else:
                break
        return head

