from collections import Counter

def customSortString(order, s): 
  counter = Counter(s)
  res = ''
  
  for c in order:
    if c in counter:
      res += c * counter[c]
      del counter[c]
      
  for c in counter:
    res += c * counter[c]
    
  print(res)

  return res


order = "bcafg"
s = "abcd" 

customSortString(order, s)