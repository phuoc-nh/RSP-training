from collections import Counter
def commonChars(words):
    def compare(a, b):
        ca = Counter(a)
        cb = Counter(b)
        res = ''
        for ka in ca:
            if ka in cb:
                res += ka * min(cb[ka], ca[ka])
                
        return res
    
    common = words[0]
    for i in range(1, len(words)):
        common = compare(common, words[i])
        
    
    
    print(list(common))
    return list(common)

words = ["bella","label","roller"]
commonChars(words)
                