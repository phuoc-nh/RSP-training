from collections import deque
def isBipartite(graph) -> bool:
    
    visited = {}
    
    for i in range(len(graph)):
        if i in visited:
            continue
        
        queue = deque()
        queue.append((i, True)) # first state 0, second state 1
        visited[i] = True
        
        while len(queue):
            node, state = queue.popleft()
            next = not state
            # print(visited)
            for nei in graph[node]:
                if nei in visited:
                    # if visited[nei] ==
                    if visited[nei] != next:
                        return False
                    continue
                
                visited[nei] = next
                queue.append((nei, next))
    
    return True
    
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# graph = [[1,3],[0,2],[1,3],[0,2]]
res = isBipartite(graph)

print('res', res)