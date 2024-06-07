class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                cur.children[w] = TrieNode()
                cur = cur.children[w]
        
        cur.isWord = True
    
    def findWord(self, word):
        cur = self.root
        print(word)
        for i in range(len(word)):
            w = word[i]
            if w in cur.children:
                cur = cur.children[w]
                if cur.isWord:
                    return word[0:i+1]
                
            else:
                return word
                


def replaceWords(dictionary, sentence):
    trie = Trie()
    
    for d in dictionary:
        trie.addWord(d)
        
    res = []
    for s in sentence.split(' '):
        part = trie.findWord(s)
        res.append(part)
    
    print(' '.join(res))
    return ' '.join(res)

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"

replaceWords(dictionary, sentence)