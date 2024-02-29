def canVisitAllRooms(rooms):
    visited = set()
    visited.add(0)
    
    s = []
    s.append(rooms[0])

    while s:
        top = s.pop() # [1,3]
        for i in range(len(top)):
            if top[i] not in visited:
                s.append(rooms[top[i]])
                print(top[i])
                print(rooms[top[i]])
                visited.add(top[i])

    print(visited)
    return len(visited) == len(rooms)

rooms = [[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(rooms))