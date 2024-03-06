def findMinimumEqualSum(rowA, rowB):
  sumRa = sum(rowA)
  sumRb = sum(rowB)
  countZeroA = 0
  for n in rowA:
    if n == 0:
      countZeroA += 1
      
  countZeroB = 0
  for n in rowB:
    if n == 0:
      countZeroB += 1
      
  
  if countZeroA == 0 and countZeroB > 0: # mean rowA can not be changed
    if sumRb + countZeroB > sumRa:
      return -1
    else:
      return max(sumRa + countZeroA, sumRb + countZeroB)
  elif countZeroA > 0 and countZeroB == 0: # mean rowB can not be changed
    if sumRa + countZeroA > sumRb:
      return -1
    else:
      return max(sumRa + countZeroA, sumRb + countZeroB)
  elif countZeroA == 0 and countZeroB == 0:
    return max(sumRa + countZeroA, sumRb + countZeroB)
  elif countZeroA > 0 and countZeroB > 0:
    return max(sumRa + countZeroA, sumRb + countZeroB)
      
rowA = [1,0,2]
rowB = [1,3,0,0]

print(findMinimumEqualSum(rowA, rowB))