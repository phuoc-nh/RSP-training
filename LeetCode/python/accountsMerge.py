def accountsMerge(accounts):
    # I can notice that
    # build list of Union Find email
    # From the list build connected emails
    # since each email map with an index and index of account -> we can trace back whose owes the email
    # How to from union find list, collect all connected emails
    
    # n = len(accounts)
    # # build Union find
    # parents = [i for i in range(n)]
    # ranking = [1 for i in range(n)]
    
    # def find(u):
    #     while u != parents[u]:
    #         u = parents[u]
        
    #     return u
    
    # def join(u, v):
    #     pu = find(u)
    #     pv = find(v)
        
    #     if pu == pv: # no need to join
    #         return False
        
    #     if ranking[pu] > ranking[pv]: # make pu parent of pv
    #         parents[pv] = pu
    #         # increase ranking
    #         ranking[pu] += ranking[pv]
    #     else:
    #         parents[pu] = pv
    #         ranking[pv] += ranking[pu]
            
    #     return True

    # emailToAcc = {}
    
    # for i in range(n):
    #     for email in accounts[i][1:]: # remove the first element
    #         if email in emailToAcc:
    #             join(i, emailToAcc[email])
    #         else:
    #             emailToAcc[email] = i
    
    # groups = {}
    # for email in emailToAcc:
    #     accountId = emailToAcc[email]
    #     # find parent
    #     parent = find(accountId)
    #     if parent not in groups:
    #         groups[parent] = []
        
    #     groups[parent].append(email)
                
    # print(parents)
    # print(emailToAcc)
    # print(groups)
    
    # res = []
    # for k in groups:
    #     name = accounts[k][0]
    #     res.append([name] + sorted(groups[k]))
    
    # print(res)
    # return res
    
    
    # ======================== DFS =====================
    # Map each email with a node by id
    # emails in the same account are connected
    # dfs through all the email to get connected paths
    # return the result
    n = len(accounts)
    nodeId = 0
    emailToId = {} # (id, accountName) for building adjacency list
    idToEmail = [] # for dfs traversing
    
    for i in range(n):
        for email in accounts[i][1:]:
            if email not in emailToId:
                emailToId[email] = (nodeId, accounts[i][0])
                idToEmail.append((email, accounts[i][0]))
                nodeId += 1
                
    print(emailToId)
    print('idToEmail', idToEmail)
    # build adjacency list, 2 emails in the same account connected
    adj = [[] for i in range(nodeId)]
    
    for acc in accounts:
        acc = acc[1:]
        for i in range(1, len(acc)):
            email1 = acc[i]
            email2 = acc[i-1]
            
            id1 = emailToId[email1][0]
            id2 = emailToId[email2][0]
            
            adj[id1].append(id2)
            adj[id2].append(id1)
            
    visited = set()
    
    def dfs(i, path):
        visited.add(i)
        path.append(idToEmail[i])
        for v in adj[i]:
            if v not in visited:
                dfs(v, path)
            
    print(adj)
    ret = []
    for k in emailToId:
        if k not in visited:
            path = []
            id = emailToId[k][0]
            dfs(id, path)
            
            # print(path)
            temp = []
            if len(path):
                for p in path:
                    temp.append(p[0])
                # temp = [path[0][1]] + temp
                print('>>>>', temp)
                ret.append([path[0][1]] + sorted(temp))
                
    print(ret)
    return  ret   
accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

accountsMerge(accounts)