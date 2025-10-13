

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
    
    
    
    emailToId = {}
    idToEmail = {}
    idToUser = {}
    count = 0
    for emails in accounts:
        for i in range(1, len(emails)):
            if emails[i] not in emailToId:
                emailToId[emails[i]] = count
                idToEmail[count] = emails[i]
                idToUser[count] = emails[0]
                count += 1
            
            
    adj = [[] for i in range(count)]
    
    
    for emails in accounts:
        for i in range(1, len(emails) - 1):
            id1 = emailToId[emails[i]]
            id2 = emailToId[emails[i+1]]
            adj[id1].append(id2)
            adj[id2].append(id1)
    

    def dfs(i, group):
        if i in visited:
            return

        visited.add(i)
        group.append(i)
        for nei in adj[i]:
            dfs(nei, group) 


    visited = set()
    groups = []
    for i in range(count):
        if i not in visited:
            group = []
            dfs(i, group)
            # toString = [idToUser[i]]
            toString = []
            for id in group:
                toString.append(idToEmail[id])
            toString.sort()
            name = idToUser[i]
            toString.insert(0, name)
            groups.append(toString)
    
    # print(idToEmail)    
    # print(idToUser)    
    # print(groups)    
    
    return groups
    
    
    
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accountsMerge(accounts)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j < len(p) - 1 and p[j+1] == '*':
                # skip
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i+1, j))
                return cache[(i, j)]
                # not skip but has to match
            
            if match:
                cache[(i, j)] = dfs(i+1, j+ 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)