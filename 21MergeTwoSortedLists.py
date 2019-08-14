# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        # add l2 into l1, so set current to be l1
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l2:
            val = l2.val
            while cur:
                if not cur.next or cur.next.val >= val:
                    node = ListNode(val)
                    node.next = cur.next
                    cur.next = node
                    break
                cur = cur.next
            l2 = l2.next
        return dummy.next


