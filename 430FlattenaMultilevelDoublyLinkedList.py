"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur = head
        while cur:
            if cur.child:
                n = cur.next
                ch = cur.child
                while ch.next:
                    ch = ch.next
                ch.next = n
                if n:
                    n.prev = ch
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            cur = cur.next
        return head
"""
Use a stack. Whenever meet node with child, push next, then build connections with child 
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        stack = []
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur
            elif not cur.next and len(stack)>0:
                cur.next = stack.pop()
                cur.next.prev = cur
            cur = cur.next
        return head