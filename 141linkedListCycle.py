# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        curr = head
        dic = {}
        pos = 0
        while curr != None:
            if curr in dic:
                return True
            else:
                dic[curr] = 1
                curr = curr.next
                pos += 1
        return False
##########################################3
## slow fast pointers
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow!=fast:
            if fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return True