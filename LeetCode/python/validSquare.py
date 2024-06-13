def validSquare(p1, p2, p3, p4):
    listP = [p1, p2, p3, p4]
    listP.sort()
    
    def dist(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    
    p1p2 = dist(listP[0], listP[1])
    p3p4 = dist(listP[2], listP[3])
    
    p2p4 = dist(listP[1], listP[3])
    p1p3 = dist(listP[0], listP[2])
    
    p2p3 = dist(listP[1], listP[2])
    p1p4 = dist(listP[0], listP[3])
    
    enumerate()
    
    return p1p2 == p3p4 and p2p4 == p1p3 and p2p3 == p1p4 and p1p3 == p1p2

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,12]
res = validSquare(p1, p2, p3, p4)
print(res)