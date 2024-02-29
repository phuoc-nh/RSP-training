# The algorithm to join small group of element into a big group

MAX = 20 # max vertex could be possible get from input
parent = [i for i in range(MAX)] # Initially, parent node of each node is itself

def unionSet(u, v): # 1 Join elements if already joined -> not do anything
    up = findSet(u)
    uv = findSet(v)

    parent[up] = uv
def findSet(u): # 2 Check 2 elemnt joined or not
    while parent[u] != u:
        u = parent[u]
    return u

query = int(input())

for i in range(query):
    u, v, q = map(int, input().split())
    
    if q == 1:
        unionSet(u, v)
    elif q == 2:
        up = findSet(u)
        uv = findSet(v)
        if up == uv:
            print("JOINED")
        else:
            print("NOT JOINED")

parent = [0, 2, 3, 3]
   
def pathCompress(u):
    if parent[u] != u:
        parent[u] = pathCompress(parent[u])
    
    return parent[u]
print(pathCompress(1))
print(findSet(1))
print(parent)