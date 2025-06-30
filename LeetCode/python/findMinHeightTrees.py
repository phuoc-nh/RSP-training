from collections import deque
def findMinHeightTrees(n, edges):
    # find leaves node
    # leave nodes have single ingress
    # BFS TRaverse from leaf nodes into the root
    # every iteration, remove edges of inside nodes by one
    # if the node has one edge, put it into the queue for the next iteration
    # the while loop will stop when there is only 1 or 2 nodes left
    # return the remaining nodes
    adj = [[] for i in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # other nodes
    # print(adj)
    edge_count = {}
    queue = deque()
    for i in range(len(adj)):
        if len(adj[i]) == 1:
            queue.append(i)
        
        edge_count[i] = len(adj[i])
            
    # print('leafNodes' , leafNodes)
    # print('inside nodes ', nodes)
    
    # run bfs
    print('n', n)
    while n > 2:
        size = len(queue)
        # print('in while queue', queue)
        for i in range(size):
            cur = queue.popleft()
            n -= 1
            for v in adj[cur]:
                edge_count[v] -= 1
                if edge_count[v] == 1:
                    queue.append(v)
    
    
    print('res', queue)
    return list(queue)        
    
    

n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]


findMinHeightTrees(n ,edges)
		
		