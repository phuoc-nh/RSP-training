def countPrefixSuffixPairs(words) -> int:
    def isPrefixAndSuffix(str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        
        if len1 > len2:
            return False
        
        return str1 == str2[0:len1] and str1 == str2[len2-len1:]
    
    
    # isPrefixAndSuffix('ab', 'aba')
    
    res = 0
    
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            # print(words[i], words[j])
            if isPrefixAndSuffix(words[i], words[j]):
                res += 1
                
    print(res)
    return res
    
    
words = ["pa","papa","ma","mama"]

countPrefixSuffixPairs(words)