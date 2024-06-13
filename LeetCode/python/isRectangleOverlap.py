def isRectangleOverlap(rec1, rec2):
    # [x1, y1, x2, y2]
    overlapX = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
    overlapY = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
    
    if overlapX <= 0 or overlapY <= 0: return False
    return True

rec1 = [0,0,1,1]
rec2 = [2,2,3,3]

print(isRectangleOverlap(rec1, rec2))