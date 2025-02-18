def numTilePossibilities(tiles: str) -> int:
    res = set()
    visited = set()
    def backtrack(i, cur):
        # if i >= len(tiles):
        #     return
        
        if len(cur):
            res.add(''.join(cur))                
        for j in range(len(tiles)):
            if j in visited:
                continue
            
            cur.append(tiles[j])
            visited.add(j)
            backtrack(j, cur)
            cur.pop()
            visited.remove(j)
        
        
    backtrack(0, [])
    
    print(res)
    print(len(res))
    
    
    return len(res)
    
tiles = "AAABBC"

# "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
numTilePossibilities(tiles)