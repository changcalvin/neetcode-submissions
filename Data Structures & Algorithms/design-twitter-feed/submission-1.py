class Twitter:

    def __init__(self):
        self.time = 0
        # userId -> [(time, tweetId), ...]
        self.tweets = defaultdict(list)
        # userId -> {followeeId, ...}
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        users = self.following[userId] | {userId} # 取并集

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]

                heapq.heappush(heap, (-time, tweetId, uid, index))
        
        while heap and len(res) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)
            res.append(tweetId)
            if index > 0:
                index -= 1
                time, tweetId = self.tweets[uid][index]
                
                heapq.heappush(heap, (-time, tweetId, uid, index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
