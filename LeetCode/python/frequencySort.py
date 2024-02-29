from collections import Counter

def frequencySort(s):
    c = Counter(s)
    listC = [[k, v] for k,v in c.items()]
    sortedS = sorted(c.items(), key=lambda x: x[1], reverse=True)
    print(sortedS)
    res = ''
    for el in sortedS:
        for _ in range(el[1]):
            res += el[0]
    return res
    print(res)
s = 'tree'

frequencySort(s)