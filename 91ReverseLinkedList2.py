# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        pre = dummy   # the m-1th node
        count = 1
        while count < m:
            pre = pre.next
            count += 1
        cur = pre.next
        m_node = cur
        past = cur.next
        while count < n:
            temp = past.next
            past.next = cur
            cur, past = past, temp
            count += 1
        m_node.next = past
        pre.next = cur
        return dummy.next