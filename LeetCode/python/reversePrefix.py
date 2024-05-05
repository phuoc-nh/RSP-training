def reversePrefix(word, ch):
    chIndex = -1
    
    for i in range(len(word)):
        if word[i] == ch:
            chIndex = i
            break
    
    if chIndex == -1:
        return word
    
    l = 0
    r = chIndex
    word = list(word)
    
    while l < r:
        word[l], word[r] = word[r], word[l]
        l += 1
        r -= 1
    return ''.join(word)
word = "abcdefd"
ch = "d"
reversePrefix(word, ch)

        