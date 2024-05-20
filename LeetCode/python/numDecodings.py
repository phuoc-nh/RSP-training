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
    
    if s[0] == '0':
        return 0
    dp = [0 for i in range(len(s))]
    dp[0] = 1
    
    for i in range(1, len(s)):
        if s[i] == '0':
            if (s[i-1] == '1' or s[i-1] == '2'):
                if i >= 2:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 1
            else:
                dp[i] = 0
        
        else:
            print('>', i)
            dp[i] += dp[i-1]
            if i == 1:
                if s[i-1] + s[i] in m:
                    dp[i] += dp[i-1]
            else:
                if s[i-1] + s[i] in m:
                    dp[i] += dp[i-2]
    
    print(dp)
    return dp[-1]       

print(numDecodings('1201234'))