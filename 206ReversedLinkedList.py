# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Build a new linked list
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # head of result list
        res = ListNode(None)
        # first node of result
        first = res.next
        while head:
            res.next = ListNode(head.val)
            res.next.next = first
            first = res.next
            head = head.next
        return res.next


# Dynamic Programming

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        curr = head
        prev = None
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr


# Better DP but change the head
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev  # Can't be curr


# Recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head)

    # recursive function, default prev = None
    def reverse(self, curr: ListNode, prev: ListNode = None):
        # break condition
        if not curr:
            return prev
        # store the next node of current node
        next_node = curr.next
        # reverse the link
        curr.next = prev
        # call function to change the link between next current and next next
        return self.reverse(next_node, curr)
