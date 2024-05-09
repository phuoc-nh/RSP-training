def findRelativeRanks(score):
    sortedScore = score.copy()
    sortedScore.sort(reverse=True)
    m = {}
    for i in range(len(sortedScore)):
        if i == 0:
            m[sortedScore[i]] = 'Gold Medal'
        elif i == 1:
            m[sortedScore[i]] = 'Silver Medal'
        elif i == 2:
            m[sortedScore[i]] = 'Bronze Medal'
        else:
            m[sortedScore[i]] = str(i+1)
    res = []
    for s in score:
        res.append(m[s])
      
    return res    
score = [5,4,3,2,1]
findRelativeRanks(score)