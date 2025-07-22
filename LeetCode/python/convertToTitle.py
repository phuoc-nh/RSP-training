def convertToTitle(columnNumber: int) -> str:
    # chr(ord('A') + offset)
    res = []
    while columnNumber > 0:
        columnNumber -= 1
        offset = columnNumber % 26
        res.append(chr(ord('A') + offset))
        columnNumber = columnNumber// 26
        
    return ''.join(reversed(res))