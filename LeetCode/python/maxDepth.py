def maxDepth(s):
  stack = []
  res = 0
  
  for el in s:
    if el == '(':
      stack.append(el)
      res = max(len(stack), res)
    elif el == ')':
      stack.pop()
      
    else:
      res = max(len(stack), res)
  
  print(res)

  return res
s = "(1)+((2))+(((3)))"
maxDepth(s)