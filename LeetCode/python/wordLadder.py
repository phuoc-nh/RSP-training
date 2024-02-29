from queue import Queue

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    res = 0
    wordList.append(beginWord)
    hm = {}
    
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            if pattern not in hm:
                hm[pattern] = [word]
            else:
                hm[pattern].append(word)
    
    print(hm)
    
    visited = set()
    q = Queue()
    
    q.put(beginWord)
    visited.add(beginWord)

    while not q.empty():
        for i in range(q.qsize()):
            word = q.get()
            if word == endWord:
                return res+1
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                for w in hm[pattern]:
                    if w not in visited:
                        q.put(w)
                        visited.add(w)
        res += 1
    print('>>>>',res)
    return res+1

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))


    