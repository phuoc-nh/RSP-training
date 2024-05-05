# def numRescueBoats(people, limit):
#     people.sort()
#     print(people)
#     l = 0
#     r = len(people) - 1
#     res = 0
#     while l <= r:
#         load = 0
#         count = 0
#         while load < limit:
#             print('count', count)
#             if l > r or count > 2:
#                 break
#             if load + people[r] <= limit:
#                 print('left', l)
#                 print('right', r)
#                 print('load', load)
#                 load += people[r]
#                 r -= 1
#                 count += 1
#             else:
#                 if load + people[l] <= limit:
#                     print('leftt', l)
#                     print('rightt', r)
#                     print('loadd', load)
#                     load += people[l]
#                     l += 1  
#                     count += 1
#                 else:
#                     break
#         print('=========')
#         res += 1
    
#     print(res)
#     return res

def numRescueBoats(people, limit):
    people.sort()
    l = 0
    r = len(people) - 1
    print(people)
    res = 0
    while l <= r:
        load = 0
        load += people[r]
        r -= 1
        if load + people[r] > limit:
            if load + people[l] <= limit:
                load += people[l]
                l += 1
        else:
            load += people[r]
            r -= 1
        res += 1
    
    print(res)
    return res

people = [3,2,3,2,2]
limit = 6
numRescueBoats(people, limit)