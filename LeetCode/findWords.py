class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for w in word:
            if w not in self.children:
                temp.children[w] = TrieNode()
            cur = cur.children[w]
        
        cur.isWord = True


def findWords(board, words):
    