class NodeTrie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.head = NodeTrie()
        
    def addWord(self, word):
        cur = self.head
        for w in word:
            if w not in cur.children:
                cur.children[w] = NodeTrie()

            cur = cur.children[w]
        
        cur.isWord = True
        
    def search(self, word):
        
        def dfs(head, j):
            cur = head
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(child, j+1):
                            return True
                    return False
                else:
                    if word[i] in cur.children:
                        cur = cur.children[word[i]]
                    else:
                        return False
            
            return cur.isWord
        
        return dfs(self.head, 0)

    