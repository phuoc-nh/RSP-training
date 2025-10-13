def intervalIntersection(firstList, secondList) :
	i = 0
	j = 0
	res = []
	while i < len(firstList) and j < len(secondList):
		s1, e1 = firstList[i]
		s2, e2 = secondList[j]
		print(i, j)
		print(s1, e1)
		print(s2, e2)
		
		if e1 < s2:
			i += 1
			continue
		
		if e2 < s1:
			j += 1
			continue
			
		res.append([max(s1, s2), min(e1, e2)])
		
		if e1 <= e2:
			i += 1
		else:
			j += 1
   
	print(res)
	return res

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

intervalIntersection(firstList, secondList)