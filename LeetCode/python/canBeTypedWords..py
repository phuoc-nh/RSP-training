def canBeTypedWords(text, brokenLetters):
    res = 0
    for t in text.split(' '): # len(word in text) * len(brokenLetters)
        containBroken = False
        for b in brokenLetters:
            if b in t:
                containBroken = True
        
        if not containBroken:
            res+=1
    # print(res)            
    return res

text = "hello world"
brokenLetters = "ad"

canBeTypedWords(text, brokenLetters)