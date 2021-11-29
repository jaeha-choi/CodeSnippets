class Node:
    def __init__(self, end=False):
        self.end = end
        self.data = {}


class Trie:

    def __init__(self):
        self.dummy = Node()

    def insert(self, word: str) -> None:
        curr = self.dummy
        for char in word:
            if char not in curr.data:
                curr.data[char] = Node()
            curr = curr.data[char]
        curr.end = True

    def _helper(self, word: str):
        curr = self.dummy
        for char in word:
            if char not in curr.data:
                return False, None
            curr = curr.data[char]
        return True, curr

    def search(self, word: str) -> bool:
        found, res = self._helper(word)
        return found and res.end

    def startsWith(self, prefix: str) -> bool:
        found, _ = self._helper(prefix)
        return found

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
