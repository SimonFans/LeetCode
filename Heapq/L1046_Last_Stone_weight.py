# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0.


# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.


# Input: stones = [1]
# Output: 1


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones => [2,7,4,1,8,1]
        # stones => [-8,-7,-4,-2,-1,-1]
        for i in range(len(stones)):
            stones[i] *= -1
        # heapify: convert list to heap, the minimum value at index 0
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 == stone_2:
                continue
            else:
                heapq.heappush(stones, stone_1 - stone_2)
        if not stones:
            return 0
        else:
            return -heapq.heappop(stones)

# O(NlogN)

