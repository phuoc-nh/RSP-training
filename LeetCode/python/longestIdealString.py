def longestIdealString(s, k):
    map = {}
    res = 1
    
    def customOrd(char):
        return ord(char) - 97 + 1
	
    for char in s :
        # print(char)
        numChar = customOrd(char)
        # map[numChar] = 1
        # for i in range(numChar+1, numChar + k + 1):
        #     if i > 26:
        #         continue
        #     if i in map:
        #         map[numChar] = max(map[numChar], 1 + map[i])
        
        # for i in range(numChar - k - 1, numChar):
        #     if i <= 0:
        #         continue
        #     if i in map:
        #         map[numChar] = max(map[numChar], 1 + map[i])
        temp = 1
        for i in range(numChar - k - 1, numChar + k + 1):
            if i > 26 or i <= 0:
                continue
            if i in map:
                temp = max(temp, 1 + map[i])
                
        if numChar in map:
            map[numChar] = max(map[numChar], temp)
        else:
            map[numChar] = temp
        res = max(res, temp)
        # print(map)
    # charMap = {}
    # for m in map:
    #     char = chr(m + 97 - 1) 
    #     charMap[char] = map[m]
    # print(charMap)
    
    print(res)
    return res
    
s = "abcd"
k = 3

longestIdealString(s, k)

# m = {
# 		'A': 1,
# 		'B': 2,
# 		'C': 3,
# 		'D': 4,
# 		'E': 5,
# 		'F': 6,
# 		'G': 7,
# 		'H': 8,
# 		'I': 9,
# 		'J': 10,
# 		'K': 11,
# 		'L': 12,
# 		'M': 13,
# 		'N': 14,
# 		'O': 15,
# 		'P': 16,
# 		'Q': 17,
# 		'R': 18,
# 		'S': 19,
# 		'T': 20,
# 		'U': 21,
# 		'V': 22,
# 		'W': 23,
# 		'X': 24,
# 		'Y': 25,
# 		'Z': 26,
# 	}