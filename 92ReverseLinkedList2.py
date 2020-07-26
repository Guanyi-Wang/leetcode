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

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    """
    1->2->...  m-1  ->  m  ->  m+1  ->  m+2  ...  ->  n  -> n+1  -> ... ->  None
               prev    cur   first     secondsecond       nth   last
    1->2->...  m-1  ->  m  ->  m+1  ->  m+2  ...  ->  n-1  ->  n  -> n+1 or None   -> ... ->  None
               prev                                            cur   first     second       nth   last
    """

    class Solution:
        def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
            if not head:
                return None
            if n == m:
                return head
            dummy = ListNode(0, head)
            prev = dummy
            for _ in range(m - 1):
                prev = prev.next
            cur = prev.next
            count = 0
            first = cur.next
            second = cur.next.next
            while count < n - m:
                first.next = cur
                cur = first
                first = second
                second = second.next if second else None
                count += 1
            prev.next.next = first
            prev.next = cur
            return dummy.next

