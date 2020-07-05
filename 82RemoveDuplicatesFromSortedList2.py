# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next.next:
            if cur.next.val == cur.next.next.val:
                dup = cur.next
                while dup.val == dup.next.val:
                    dup = dup.next
                    if not dup.next:  # duplicates at the end [2,3,3,3]
                        cur.next = None
                        return dummy.next
                dup = dup.next
                cur.next = dup
            else:
                cur = cur.next
        return dummy.next