class TreeNode:
    def __init__(self):
        # 26 slots for 'a' to 'z'
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # Initialize the root node
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root  # Start from root node
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = TreeNode()
            node = node.children[index]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node is not None

    def _search_prefix(self, prefix: str):
        node = self.root  # Start from root
        for char in prefix:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                return None  # No such prefix
            node = node.children[index]
        return node  # Return the node at the end of prefix
