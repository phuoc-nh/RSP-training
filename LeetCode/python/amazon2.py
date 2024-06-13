# def solution(retailers, requests):
#     res = []
#     for x1, y1 in requests:
#         count = 0
#         for x2, y2 in retailers:
#             if x1 <= x2 and y1 <= y2:
#                 count += 1
#         res.append(count)
#     # print(res)
#     return res
# retailers = [[1,2], [2,3], [1,5]]
# requests = [[1,1], [1,4]]
# # [3, 1] returned

# solution(retailers, requests)


def solution(power, minPower, maxPower):
    intervals = []
    for i in range(len(minPower)):
        intervals.append([minPower[i], maxPower[i]])
    intervals.sort()
    power.sort()
    print(intervals)
    print(power)
    res = []

    for l, r in intervals:
        numb = 0
        total = 0
        i = 0
        print('left', l)
        print('right', r)
        print('power', power[i])
        while i < len(power) :
            if power[i] >= l and power[i] <= r:
                numb += 1
                total += power[i]
            i += 1
        res.append([numb, total])
    print(res)
    return res
        
power = [7,6,8,10]
minPower = [6, 3, 4]
maxPower = [10, 7, 9]

solution(power, minPower, maxPower)


# # Write your code here
intervals = []
for i in range(len(minPower)):
    intervals.append([minPower[i], maxPower[i]])

res = []
# [6, 10]
# 6,7,8,10
for l, r in intervals:
    numb = 0
    total = 0
    for p in power:
        if p >= l and p <= r:
            numb += 1
            total += p
    res.append([numb, total])
# print(res)
return res