def distinctNames(ideas) -> int:
    # observation 2 words with same initial could not form a result
    groups = {}
    # notice that 2 words has the same suffix could not form a result either
    # we need to compare suffix without initial
    for word in ideas:
        initial = word[0]
        if initial not in groups:
            groups[initial] = set()
        groups[initial].add(word[1:])

    res = 0
    for g1 in groups:
        for g2 in groups:
            if g1 == g2:
                continue
            # find intersect words
            intersect = 0
            for word in groups[g1]:
                if word in groups[g2]:
                    intersect += 1
            
            # result between 2 groups equal len group minus intersect multipy other group
            res += (len(groups[g1]) - intersect) * (len(groups[g2]) - intersect)
    
    # print(res)
    # print(groups)
    return res
            
    
ideas = ["coffee","donuts","time","toffee"]

distinctNames(ideas)