
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.nodes:
                cur.nodes[ch] = Trie()
            cur = cur.nodes[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.nodes:
                return False
            else:
                cur = cur.nodes[ch]

        return cur.isEnd
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self
        for ch in prefix:
            if ch in cur.nodes:
                cur = cur.nodes[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)