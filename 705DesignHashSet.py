class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [None] * self.size

    def add(self, key: int) -> None:
        hash_value = self.hash(key)
        cur = self.buckets[hash_value]
        if not cur:
            self.buckets[hash_value] = ListNode(key, None)
            return
        if cur.val == key:
            return
        while cur:
            if cur.val == key:
                return
            if not cur.next:
                cur.next = ListNode(key, None)
                return
            cur = cur.next
        return

    def remove(self, key: int) -> None:
        hash_value = self.hash(key)
        cur = self.buckets[hash_value]
        if not cur:
            return
        if cur.val == key:
            self.buckets[hash_value] = cur.next
            return
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return
        # prev = cur
        # cur = cur.next
        # while cur:
        #     if cur.val == key:
        #         prev = cur.next
        #         return
        #     prev = cur
        #     cur = cur.next
        # return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_value = self.hash(key)
        cur = self.buckets[hash_value]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    def hash(self, key: int) -> int:
        return key % self.size

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)