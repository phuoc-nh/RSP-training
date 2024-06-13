def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2- bx1) * (by2 - by1)
    print(area1, area2)
    # calculate overlap
    x1 = min(ax2, bx2) - max(bx1, ax1)
    print(x1)
    y1 = min(ay2, by2) - max(by1, ay1)
    print(y1)
    overlap = 0
    if x1 > 0 and y1 > 0:
        overlap = x1 * y1
    
    return area1 + area2 - overlap
ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = -2
by1 = -2
bx2 = 2
by2 = 2

res = computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
print(res)