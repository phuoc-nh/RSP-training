# from collections import Counter
# from queue import PriorityQueue
# class Count:
#     def __init__(self, num, count):
#         self.num = num
#         self.count = count

#     def __lt__(self, other):
#         return self.count <= other.count


# def findLeastNumOfUniqueInts(arr, k):
#     c = Counter(arr)
#     pq = PriorityQueue()
    
#     for key, v in c.items():
#         pq.put(Count(key, v))

#     # top = pq.get()
    
#     while k > 0 and not pq.empty():
#         k -= pq.queue[0].count
#         if k >= 0:
#             pq.get()
    
#     print(pq.queue)
#     print(len(pq.queue))
    
#     return len(pq.queue)
from collections import Counter
def findLeastNumOfUniqueInts(arr, k):
    bucket = [[] for i in range(len(arr)+1)]
    counter = Counter(arr)

    for key, count in counter.items():
        bucket[count].append(key)

    res = len(counter.keys())
    # print(bucket)
    # print('res', res)
    
    for i in range(len(bucket)):
        for j in bucket[i]:
            print('k', k)
            print('i', i)
            if k >= i:
                res -= 1
                k -= i

    # print(res)
    return res



arr = [1]
k = 1
findLeastNumOfUniqueInts(arr, k)
    