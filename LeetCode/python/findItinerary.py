from collections import deque
def findItinerary(tickets):
    # difficulties
    # usually, dfs/bfs visited each node once and moveon
    # this task one node may be visited multple times
    # in order to solve it, every time visit a node, remove the path connecting that node in adj list
    # another difficult issue is
    # let say if a path could not reach to final destination
    # we need to trace back to previous node and follow a new path
    # that why we need to backtrack in this task
    # lastly, how to move between destinations in lexical order
    # just sort the list and then all the adj will search the sorted lexical order first
    
    adj = {}
    for dept, dest in tickets:
        adj[dept] = []
        adj[dest] = []
    tickets.sort()
    for dept, dest in tickets:
        adj[dept].append(dest)
        
    # print(adj)
    res = ['JFK']
    
    # queue = deque()
    
    def dfs(src):
        if len(res) == len(tickets) + 1: # finish all the path
            return True

        if len(adj[src]) == 0:
            # meaning that we dont have tickets to get out of this node
            # although we have not finished all the nodes
            return False
        temp = adj[src].copy()
        for i in range(len(temp)):
            dest = temp[i]
            res.append(dest)
            # temporarily remove path in the adj
            adj[src].pop(i)
            # recursion
            if dfs(dest):
                return True
            
            # backtrack remove last result instance, and add back path in adj
            res.pop()
            a = []
            adj[src].insert(i, dest)
            
        return False
    
    dfs('JFK')
    
    print('res', res)
    
    return res
    
    
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

findItinerary(tickets)