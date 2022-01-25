'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
  
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # find out how many valid positions that we can place flowers
        
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i] == 0 and f[i+1] == 0 and f[i-1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0
      
      
#         i, count = 0, 0 
#         while i < len(flowerbed):
#             if flowerbed[i] ==0 and (i ==0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 count += 1
#             i+=1
#         return count >= n
