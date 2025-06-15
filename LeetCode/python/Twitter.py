import heapq
class Twitter:

    def __init__(self):
        self.followMap = {}
        self.postId = 0
        self.tweetsMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetsMap:
            self.tweetsMap[userId] = []
            
        self.tweetsMap[userId].append((tweetId, self.postId))
        self.postId -= 1 # use min heap, prioritise later postId

    def getNewsFeed(self, userId: int):
        # get follows
        if userId not in self.followMap:
            ids = []
        else:
            ids = list(self.followMap[userId])
            
        ids.append(userId)
        # get all tweets from ids list
        res = []
        
        heap = []
        for id in ids:
            if id not in self.tweetsMap:
                continue
            tweets = self.tweetsMap[id]
            if not len(tweets):
                continue
            # get last tweet
            lastIndex = len(tweets) - 1
            heap.append((tweets[lastIndex][1], tweets[lastIndex][0], id, lastIndex)) # postIdCount, tweetId, userId, lastIndex
        
        heapq.heapify(heap)
        
        while len(heap):
            _, tweetId, userId, lastIndex = heapq.heappop(heap)
            res.append(tweetId)
            if len(res) == 10:
                return res
            
            if lastIndex == 0:
                continue
                
            lastIndex -= 1
            nextTweet = self.tweetsMap[userId][lastIndex]
            
            heapq.heappush(heap, (nextTweet[1], nextTweet[0], userId, lastIndex))
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            return

        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,1)
param_2 = obj.getNewsFeed(1)
obj.follow(1,2)
obj.unfollow(1,3)