# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Generate two list, one(f) stores all nums less than x, one(s) contains others. Combine them.
        """
        f_head = ListNode()
        s_head = ListNode()
        f = f_head
        s = s_head
        cur = head
        while cur:
            if cur.val < x:
                f.next = cur
                f = f.next
            else:
                s.next = cur
                s = s.next
            cur = cur.next
        f.next = s_head.next
        s.next = None
        return f_head.next