# 
#   def helper(num1, num2):
#     num1 = str(num1)
#     num2 = str(num2)
#     len1 = len(num1)
#     len2 = len(num2)
#     count = 0
    
#     for i in range(len1):
#       if i >= len2:
#         break
      
#       if num1[i] == num2[i]:
#         count += 1
#       else:
#         break
#     # print(count)
#     return count
#   res = 0
#   for num1 in arr1:
#     for num2 in arr2:
#       res = max(res, helper(num1, num2))
  
#   print(res)

#   return res
def longestCommonPrefix(arr1, arr2):
		
arr1 = [1,10,100]
arr2 = [1000]
longestCommonPrefix(arr1, arr2)