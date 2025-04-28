def numRescueBoats( people, limit: int) -> int:
    people.sort()
    
    boats = 0
    l = 0
    r = len(people) - 1
    print(people)
    while l <= r:
        # consider right
        capacity = limit
        capacity -= people[r]
        r -= 1
        if capacity >= people[l]:
            capacity -= people[l]
            l += 1
            
        boats +=1
        
    print('boats', boats)
        
        # then consider if we can put any more people on left side in the boat
        
    return boats
    
people = [2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10]

limit = 50

numRescueBoats(people, limit)