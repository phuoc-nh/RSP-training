def findJudge(n, trust):
    adj = [[] for i in range(n+1)]

    for t in trust:
        adj[t[0]].append(t[1])

    print(adj)
    for i in range(1, n+1):
        if not adj[i]:
            isJudge = True
            for j in range(1, n+1):
                if i == j:
                    continue
                if i not in adj[j]:
                    isJudge = False
            
            return i if isJudge else -1

    return -1
n = 2
trust = [[1,2]]
print(findJudge(n, trust))