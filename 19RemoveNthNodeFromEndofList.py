
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Traverse on time to find the length of List and then traverse again to remove nth from the end
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length  = 0
        cur = head
        dummy = ListNode(0,head) # to handle edge cases,like [1],1 or remove head
        # caculate the length
        while cur.next:
            length += 1
            cur = cur.next
        # find the nth from the end and remove it
        cur = dummy
        length = length - n +1
        while length > 0:
            length -= 1
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    """
    Two pointers solution, fast pointer lead n steps than slow pointer
    """

    class Solution:
        def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
            dummy = ListNode(0, head)
            fast = slow = dummy
            l = 0
            while fast.next:
                fast = fast.next
                l += 1
                if l > n:
                    slow = slow.next
            slow.next = slow.next.next
            return dummy.next

        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        '''
        Two pointers 
        '''

        class Solution:
            def rotateRight(self, head: ListNode, k: int) -> ListNode:
                if not head or not k:
                    return head
                if not head.next:
                    return head
                length = 1
                cur = head
                while cur.next:
                    cur = cur.next
                    length += 1  # length = 5
                # find the new head, new head start from h_th to the end
                h = k % length  # 2%5 = 2 2th to the end--[2] should be the new head
                if h == 0:
                    return head
                fast = slow = head
                for i in range(h):
                    fast = fast.next
                while fast.next:
                    fast = fast.next
                    slow = slow.next
                tail = slow  # [3]
                new_head = tail.next  # [4]
                fast.next = head  # [5]->[1]
                tail.next = None  # [3]-> None
                return new_head  # [4]
