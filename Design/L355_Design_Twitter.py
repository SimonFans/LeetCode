'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


'''

import collections
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        # used for heap later. {'user_id':[(time, tweets_id)]}
        self.messages = collections.defaultdict(list)
        # following set
        self.following = collections.defaultdict(set)
        # Given by question
        self.__number_of_most_recent_tweets = 10
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.messages[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # use heapq 
        # maxHeap: (-1* most recent time, userId, # of tweers current userId had)
        maxHeap = []
        # save returned tweetsId
        result = []
        # 如果当前user发过tweets，则压入当前user最后一条发送的tweets时间, 最后的0记录当前读了多少条tweets，倒着读
        if self.messages[userId]:
            heapq.heappush(maxHeap, (-self.messages[userId][-1][0], userId, 0))
        # 找出当前user follow了哪些users
        for uid in self.following[userId]:
            # 如果当前userfollow的那些users也发了tweets
            if self.messages[uid]:
                heapq.heappush(maxHeap, (-self.messages[uid][-1][0], uid, 0))
        # 查找最近的10条tweets
        while maxHeap and len(result) < self.__number_of_most_recent_tweets:
            _time, _uid, _curr = heapq.heappop(maxHeap)
            _next = _curr + 1
            if _next < len(self.messages[_uid]):
                heapq.heappush(maxHeap, (-self.messages[_uid][-(_next+1)][0], _uid, _next))
            # append当前时间最近的user_id对应的tweets
            result.append(self.messages[_uid][-(_curr+1)][1])
        return result
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
