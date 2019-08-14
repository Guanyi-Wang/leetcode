# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        cur = res
        p = l1
        q = l2
        carry = 0
        while p or q or carry:
            x = 0
            y = 0
            if p:
                x = p.val
                p = p.next
            if q:
                y = q.val
                q = q.next
            s = x + y + carry
            carry = int(s/10)
            sum = s%10
            cur.next = ListNode(sum)
            cur = cur.next
        return res.next