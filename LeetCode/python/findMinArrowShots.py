def findMinArrowShots(points):
	points.sort()
	arrows = 1
	prev = points[0]

	for i in range(1, len(points)):
		if points[i][0] <= prev[1]:
			prev = [points[i][0], min(points[i][1], prev[1])]
		else:
			arrows += 1
			prev = points[i]
	print(arrows)
	return arrows


points = [[10,16],[2,8],[1,6],[7,12]]
findMinArrowShots(points)