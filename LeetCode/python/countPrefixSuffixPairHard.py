class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = Node()
        self.count = 0
        
    def add(self, word):
        cur = self.root
        for i in range(len(word)):
            newNode = (word[i], word[len(word) - i - 1])
            
            if newNode in cur.children:
                cur = cur.children[newNode]
            else:
                cur.children[newNode] = Node()
                cur = cur.children[newNode]
                
            self.count += cur.count
            
        cur.count += 1
         
        
    
                    

def countPrefixSuffixPairs(words) -> int:
    res = 0
    trie = Trie()
    for word in words:
        trie.add(word)
        
    print(trie.count)
    
    
    return trie.count
    
    
words = ["abab","ab"]

countPrefixSuffixPairs(words)