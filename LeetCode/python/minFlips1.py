def minBitFlips(start: int, goal: int) -> int:
	res = 0
	while start or goal:
		if start % 2 != goal % 2:
			res += 1
		start = start >> 1
		goal = goal >> 1
	
	return res