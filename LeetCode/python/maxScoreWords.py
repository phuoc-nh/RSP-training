from collections import Counter

def maxScoreWords(words, letters, score):
    lettersCounter = Counter(letters)
    def inLetter(word):
        wordCounter = Counter(word)
        for w in wordCounter:
            if wordCounter[w] > lettersCounter[w]:
                return False
        
        return True
    
    def getScore(word):
        res = 0
        for w in word:
            res += score[ord(w) - ord('a')]
        return res
    
    
    def backtrack(i):
        if i == len(words):
            return 0
        
        # skip i
        res = backtrack(i+1)
      
        # include i
        if inLetter(words[i]):
            # subtract counter in letters
            for w in words[i]:
                lettersCounter[w] -= 1
            res = max(res, backtrack(i+1) + getScore(words[i]))
            # after backtrack return original count
            for w in words[i]:
                lettersCounter[w] += 1
        
        return res
    return backtrack(0)

words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

print('res', maxScoreWords(words, letters, score))