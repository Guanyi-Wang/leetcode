# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Traverse through to get the length, calculate the index of new head, find the new head and manipulate the list. Take [1,2,3,4,5], 2 as example.
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
        dummy = ListNode(0, head)  # dummy->1->2->3->4->5
        cur = dummy
        while length - h > 0:  # move foward 3 steps from dummy to [3]
            cur = cur.next
            length -= 1
        tail = cur  # [3]
        print(tail.val)
        new_head = tail.next  # [4]
        while cur.next:  # find the original tail [5]
            cur = cur.next
        cur.next = head  # [5]->[1]
        tail.next = None  # [3]-> None
        return new_head  # [4]


