def longestCommonPrefix(words):
    shortestWord = min(words, key=len)
    
    def compare2Words(s1,s2):
        i = 0
        j = 0
        res = ''
        print(s1, s2)
        while i < len(s1) and j < len(s2):
            print(i, j)
            if s1[i] == s2[j]:
                res += s1[i]
            else:
                return res
            i += 1
            j += 1
        return res

    for s in words:
        shortestWord = compare2Words(s, shortestWord)

    print(shortestWord)
    return shortestWord

strs = ["flower","flow","flight"]

longestCommonPrefix(strs)