import heapq
from collections import defaultdict


class Twitter(object):

    def __init__(self):
        self.posts = {}
        self.followers = {}
        self.time = 0


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId in self.posts:
            self.posts[userId].append([self.time, tweetId])
        self.posts[userId] = [[self.time, tweetId]]
        self.time -=1



    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        min_heap = []
        for follower_id in self.followers[userId]:
            if follower_id in self.posts:
                index = len(self.posts[follower_id]) - 1
                count, tweet_id = self.posts[follower_id][index]
                min_heap.append([count, tweet_id, follower_id, index-1])
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            count, tweet_id, follower_id, index = heapq.heappop(min_heap)
            res.append(tweet_id)
            if index >=0:
                count, tweet_id = self.posts[follower_id][index]
                heapq.heappush(min_heap, [count, tweet_id, follower_id, index-1])

        return res

        def getNewsFeed(self, userId) :
            # Merge the tweets of the user's followees (including the user) using heapq.merge
            tweets = list(heapq.merge(
                *(self.posts[followee] for followee in self.followers[userId] | {userId})))
            # Return the tweet IDs of the 10 most recent tweets
            return [tweetId for _, tweetId in tweets[:10]]



    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.followers.get(followerId):
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = set(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)