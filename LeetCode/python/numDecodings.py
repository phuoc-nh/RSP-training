def numDecodings(s):
    m = {
		'1': 'A',
		'2': 'B',
		'3': 'C',
		'4': 'D',
		'5': 'E',
		'6': 'F',
		'7': 'G',
		'8': 'H',
		'9': 'I',
		'10': 'J',
		'11': 'K',
		'12': 'L',
		'13': 'M',
		'14': 'N',
		'15': 'O',
		'16': 'P',
		'17': 'Q',
		'18': 'R',
		'19': 'S',
		'20': 'T',
		'21': 'U',
		'22': 'V',
		'23': 'W',
		'24': 'X',
		'25': 'Y',
		'26': 'Z',
	}
    
    
    dp = [0] * len(s)
    if s[0] in m:
        dp[0] = 1
        
    for i in range(1, len(s)):
        prev = s[i-1:i+1]
        # print(prev)
        
        # valid and prev valid
        if s[i] in m and prev in m:
            # print('.as')
            if i - 2 >= 0:
                
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1] + 1
        # valid, prev not valid
        if s[i] in m and prev not in m:
            dp[i] = dp[i-1]
        
        # not valid, prev not valid
        if s[i] not in m and prev not in m:
            dp[i] = 0
            
        # not valid, prev valid
        if s[i] not in m and prev in m:
            if i - 2 >= 0:
                dp[i] = dp[i-2]
            else:
                dp[i] = 1
            
        
    print(dp)
    return dp[-1]
        
  

print(numDecodings('1123'))