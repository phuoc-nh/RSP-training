# from collections import Counter

# def longestPalindrome(s):
#     counterS = Counter(s)
#     maxOdd = 0
#     maxOddChar = None
#     for c in counterS.keys():
#         if counterS[c] % 2 == 1 and counterS[c] > maxOdd:
#             maxOdd = counterS[c]
#             maxOddChar = c
    
#     res = 0
#     for c in counterS.keys():
#         if counterS[c] % 2 == 0:
#             res += counterS[c]
    
#     return res + maxOdd            

# s = "a"
# print(longestPalindrome(s))

import math

xs = [14000,13000]     # values (must be floats!)
mean = sum(xs) / len(xs)   # mean
var  = sum(pow(x-mean,2) for x in xs) / len(xs)  # variance
std  = math.sqrt(var) 
print(std)