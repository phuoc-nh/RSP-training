class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True
    def search(self, word):
        cur = self.root

        for w in word:
            if w in cur.children:
                cur = cur.children[w] 
            else:
                return False

        if cur.isWord:
            return True
        return False
    def startsWith(self, prefix):
        cur = self.root
        
        for w in prefix:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False    

        return True
trie = Trie()
trie.insert("apple")
print(trie.search("ape"))
print(trie.startsWith("app"))