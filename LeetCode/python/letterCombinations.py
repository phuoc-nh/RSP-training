def letterCombinations(digits):
    m = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    res = []
    
    def backtrack(word, remainDigits):
        if word and len(word) == len(digits):
            res.append(word)
            return
        
        for i in range(len(remainDigits)):
            for d in m[remainDigits[i]]:
                backtrack(word+d, remainDigits[i+1:])
        
    
    backtrack('', digits)
    print(res)
    return res

letterCombinations("23")
        