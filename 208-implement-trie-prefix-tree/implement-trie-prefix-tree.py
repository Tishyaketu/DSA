class TrieNode():
  def __init__(self):
    self.child = [None for _ in range(26)]
    self.isEnd = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
          idx = ord(ch) - ord('a')
          if node.child[idx] is None:
            node.child[idx] = TrieNode()
          node = node.child[idx]
        node.isEnd = True
    def searchTrie(self,param):
        node = self.root
        for ch in param:
          idx = ord(ch) - ord('a')
          if node.child[idx] is None:
            return None
          node = node.child[idx]
        return node
    def search(self, word: str) -> bool:
        node = self.searchTrie(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchTrie(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)