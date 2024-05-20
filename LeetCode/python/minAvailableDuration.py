def minAvailableDuration(slots1, slots2, duration):
    slots1.sort()
    slots2.sort()
    # print(slots1)
    i = 0
    j = 0
    while i < len(slots1) and j < len(slots2):
        s1Start, s1End = slots1[i]
        s2Start, s2End = slots2[j]
        if s1Start > s2End:
            j += 1
            continue
        if s1End < s2Start:
            i += 1
            continue
        overlap1 = max(s1Start, s2Start)
        overlap2 = min(s1End, s2End)
        
        print('overlap', [overlap1, overlap2])
        if overlap2 - overlap1 >= duration:
            return [overlap1, overlap1 + duration]
        
        if s1End < s2End:
            i += 1
        
        # elif s2End < s1End: time limit
        else: # not time limit 
            j += 1
        
    return []
    # for s1 in slots1:
    #     for s2 in slots2:
    #         s1Start, s1End = s1
    #         s2Start, s2End = s2
    #         if s1Start > s2End or s1End < s2Start:
    #             continue
            
    #         overlap1 = max(s1Start, s2Start)
    #         overlap2 = min(s1End, s2End)
            
    #         print('overlap', [overlap1, overlap2])
    #         if overlap2 - overlap1 >= duration:
    #             return [overlap1, overlap1 + duration]
    
    # return []
# slots1 = [[10,50],[60,120],[140,210]]
# slots2 = [[0,15],[60,70]]
# duration = 8

slots1 = [[10,60]]
slots2 = [[12,17],[21,50]]
duration = 8
print(minAvailableDuration(slots1, slots2, duration) )           
                