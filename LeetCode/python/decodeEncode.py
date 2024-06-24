class Codec:
    def encode(self, strs):
        encodedStr = ''
        for s in strs:
            encodedStr += str(len(s)) + '#' + s
        print(encodedStr)
        
        return encodedStr    
        
    def decode(self, s):
        print(s)
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        print(res)
        return res
# 4#love8#neetcode13#somethingElse
#   23456   
# Your Codec object will be instantiated and called as such:
strs = ['love', 'neetcode', 'somethingElse']
codec = Codec()
s = codec.encode(strs)
codec.decode(s)