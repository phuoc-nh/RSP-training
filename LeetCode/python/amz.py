# from collections import Counter
# def solution(letters):
#   cnt = Counter(letters)
#   sorted_cnt = cnt.most_common()
#   print(sorted_cnt)
#   res = 0
  
#   for i in range(len(sorted_cnt)):
#     if i >= 0 and i <= 8:
#       res += sorted_cnt[i][1] * 1
#     elif i >= 9 and i <= 17:
#       res += sorted_cnt[i][1] * 2
#     else:
#       res += sorted_cnt[i][1] * 3
      
#   return res


# letters = "abcghdiefjoba"
# solution(letters)
  
from queue import PriorityQueue
def solution(frontend, backend):
  fe_pq = PriorityQueue()
  be_pq = PriorityQueue()
  
  for el in frontend:
    fe_pq.put(el * -1)
  
  for el in backend:
    be_pq.put(el * -1)
  
  res = 0  
  
  while not fe_pq.empty() and not be_pq.empty():
    top_fe = fe_pq.queue[0] * -1
    top_be = be_pq.queue[0] * -1

    if top_fe > top_be:
      res += 1
      fe_pq.get()
      be_pq.get()
    else:
      be_pq.get()
  print(res)
  return res
    
frontend = [1,2,3,4,5]
backend = [6,6,1,1,1]

solution(frontend, backend)
      
      
    
      
  
  
  