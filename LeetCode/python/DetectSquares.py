class DetectSquares:

    def __init__(self):
        self.setPoints = {}
        self.list = []  

    def add(self, point) -> None:
        self.setPoints[(point[0], point[1])] = self.setPoints.get((point[0], point[1]), 0) + 1
        self.list.append(point)

    def count(self, point) -> int:
        res = 0
        for p1 in self.setPoints:
            p2 = (p1[0], point[1])
            p3 = (point[0], p1[1])
            # print(p1)
            # print(p2)
            print(p3)
            # compare distance
            p1p2Distance = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            p1p3Distance = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
            # print(p2 in self.setPoints)
            # print(p3 in self.setPoints)
            if p2 in self.setPoints and p3 in self.setPoints and p1p2Distance == p1p3Distance and p1[0] != point[0] and p1[1] != point[1]:
               res += self.setPoints[p2] * self.setPoints[p3]
            # print('=====')
        return res
            


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])


print(obj.count([11,10]))
print(obj.count([14,8]))

obj.add([11,2])
print(obj.count([11,10]))
# param_2 = obj.count(point)