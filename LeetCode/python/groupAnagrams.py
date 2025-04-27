def groupAnagrams(strs):
    m = {}
    res = []
    
    for s in strs:
        lists = list(s)
        lists.sort()
        str = "".join(lists)
        print("")
        if str in m:
            m[str].append(s)
        else:
            m[str] = [s]
       
    print(m)
    
    for k in m:
        res.append(m[k])
    
    print(res)
    return res

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

