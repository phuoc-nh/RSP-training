def interchangeableRectangles(rectangles):
    count =  {}
    for w, h in rectangles:
        count[w / h] = 1 + count.get(w / h, 0)
    res = 0
    for k, v in count.items():
        if v >= 2:
            res += v * (v-1) // 2
    print(res)            
    return res


rectangles = [[4,5],[7,8]]
interchangeableRectangles(rectangles)