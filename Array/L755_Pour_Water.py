'''
We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1. After volume units of water fall at index k, how much water is at each index?

Water first drops at index k and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise at it's current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the terrain plus any water in that column.

We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.


Input: heights = [2,1,1,2,1,2,2], volume = 4, k = 3
Output: [2,2,2,3,2,2,2]
Explanation:
#       #
#       #
##  # ###
#########
 0123456    <- index


The final answer is [2,2,2,3,2,2,2]:

    #    
 ####### 
 ####### 
 0123456 
 

Input: heights = [1,2,3,4], volume = 2, k = 2
Output: [2,3,3,4]
Explanation:
The last droplet settles at index 1, since moving further left would not cause it to eventually fall to a lower height.

Input: heights = [3,1,3], volume = 5, k = 1
Output: [4,4,4]


Solution:

class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        # V: 多少次滴水
        # K: 滴水的位置
        def findLeftPosition(heights, K):
            left_position = i = K
            while i > 0:
                if heights[i-1] > heights[i]:
                    break
                #不能用else是因为有当前位置和左边位置同样高的情况
                elif heights[i-1] < heights[i]:
                    #这里应该是i-1而不是left_position -= 1
                    left_position = i-1
                i -= 1
            return left_position
                    
        def findRightPosition(heights, K):
            right_position = i = K
            while i < len(heights)-1:
                if heights[i+1] > heights[i]:
                    break
                #不能用else是因为有当前位置和右边位置同样高的情况
                elif heights[i+1] < heights[i]:
                    #这里应该是i+1而不是right_position += 1
                    right_position = i+1
                i += 1
            return right_position
        
        for _ in range(V):
            left_position = findLeftPosition(heights, K)
            print(left_position)
            if left_position != K:
                heights[left_position] += 1
            else:
                right_position = findRightPosition(heights, K)
                if right_position != K:
                    heights[right_position] += 1
                else:
                    heights[K] += 1
        return heights
        

'''
