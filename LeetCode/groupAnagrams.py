def groupAnagrams(strs):
    res = []
    m = {}

    for s in strs:
        temp = s
        sortedS = ''.join(sorted(s))
        print(sortedS)
        
        if sortedS in m:
            m[sortedS].append(temp)
        else:
            m[sortedS] = [temp]            

    for k in m:
        res.append(m[k])
    print(res)
    return res

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

