"""
Trie and DFS solution.
"""


class TrieNode:
    """
    TrieNode: self.nodes:{char:TrieNode}
              self.is_end: bool
    """

    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for ch in word:
            # if ch not in cur.nodes:
            #     cur.nodes.append(ch)
            # else:
            #     cur = cur.nodes[ch]
            cur = cur.nodes[ch]
        cur.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        return self.dfs(word, self.root)

    def dfs(self, word, node):
        if not word:
            return node.is_end
        for ch in word:
            if ch == '.':
                for key in node.nodes:
                    if self.dfs(word[1:], node.nodes[key]):
                        return True
                return False
            elif ch in node.nodes:
                return self.dfs(word[1:], node.nodes[ch])
            else:
                return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)