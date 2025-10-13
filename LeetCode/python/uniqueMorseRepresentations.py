def uniqueMorseRepresentations(words) -> int:
    morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    uniqueCodes = set()
    
    for word in words:
        code = ''
        for char in word:
            print(ord('a'))
            print('morseCodes', morseCodes[ord(char) - ord('a')])
            code += morseCodes[ord(char) - ord('a')]
        uniqueCodes.add(code)
        
    return len(uniqueCodes)
words = ["gin","zen","gig","msg"]
res = uniqueMorseRepresentations(words)
print('r', res)